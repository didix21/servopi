from servopi.servomodels import ServoModel
import RPi.GPIO as GPIO
import time


class Servo(object):

    def __init__(self, rasp_pin, servo_model='', *args):

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
        self._angle = angle
        self._get_pulse_width()
        self._duty_cycle = self._get_duty_cycle()
        self._pwm.ChangeDutyCycle(self._duty_cycle)
        time.sleep(self._pulse_width / 1000)

    def write_duty_cycle(self, duty_cycle):

        self._duty_cycle = duty_cycle
        self._pwm.ChangeDutyCycle(self._duty_cycle)

    def read_angle(self):

        return self._angle

    def read_duty_cycle(self):

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

