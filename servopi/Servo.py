from servopi.servomodels import ServoModel
import RPi.GPIO as GPIO
import time


class Servo(object):
    """ Servo class offers some easy tools for working with Servo motors in raspberry pi.

    """
    def __init__(self, rasp_pin, servo_model='', *args):
        """Initialize the raspberry pin, where servo is connected, and the model of the servo.
        Setting `servo_model = 'sg90'` will set the parameters of a sg90. This means will set
        pulse width to 20 ms. Moreover will set the angle range which servo can move. In this case,
        0º til 180º. If no model is set then sg90 parameters are chosen by default. Moreover,
        servo_model allows to chose our own servo motor. This means that frequency, servo's max angle
        and servo's min pulse width can be passed through *args parameters.

        :param rasp_pin: raspberry pin or channel
        :param servo_model: avaiable models are:'mg955', 'sg90' or 'myown'.
        :param args: in case servo_model = 'myown' *args wil lbe equal to (frequency, max_angle, min_pulse_width).
        """

        self._pulse_width = 0
        self._duty_cycle = 10
        self._angle = 90
        self.rasp_pin = rasp_pin

        self.s_model = ServoModel().get_model(servo_model, *args)
        self._configure_pin(self.rasp_pin)
        self._configure_pwm()

    def __del__(self):

        GPIO.cleanup(self.rasp_pin)

    def write_angle(self, angle):
        """ This method allows to move to position set by angle.

        :param angle: the angle where servo axis has to go.
        """
        self._angle = angle
        self._get_pulse_width()
        self._duty_cycle = self._get_duty_cycle()
        self._pwm.ChangeDutyCycle(self._duty_cycle)
        time.sleep(self._pulse_width / 1000)

    def write_duty_cycle(self, duty_cycle):
        """ Move to a position setting duty cycle.

        :param duty_cycle: the value of duty cycle.
        """
        self._duty_cycle = duty_cycle
        self._pwm.ChangeDutyCycle(self._duty_cycle)

    def read_angle(self):
        """ Return the angle where servo is set.

        :return: the angle.
        """
        return self._angle

    def read_duty_cycle(self):
        """ Return the actual value of the duty cycle that has been set.

        :return: the duty cycle.
        """

        return self._duty_cycle

    def _configure_pwm(self):

        self._pwm = GPIO.PWM(self._pin, self.s_model.frequency)
        self._pwm.start(self._duty_cycle)

    def _configure_pin(self, rasp_pin):

        self._pin = rasp_pin
        GPIO.setup(self._pin, GPIO.OUT)

    def _get_pulse_width(self):

        self._pulse_width = self.s_model.m_pulse * self._angle + self.s_model.n_pulse

    def _get_duty_cycle(self):

        return self._pulse_width * self.s_model.frequency / 10.0


if __name__ == "__main__":

    newservo = Servo(1)

