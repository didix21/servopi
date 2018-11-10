
import Ser
import RPi.GPIO as GPIO
import time


class Servo(object):

    def __init__(self, rasp_pin, servo_model='', *args):

        self._pulse_width = 0
        self._duty_cycle = 10
        self._angle = 90
        self.rasp_pin = rasp_pin

        self.s_model = ServoModel().get_model(servo_model, *args)
        self.__configure_pin(self.rasp_pin)
        self.__configure_pwm()

    def __del__(self):

        GPIO.cleanup(self.rasp_pin)

    def write_angle(self, angle):
        self._angle = angle
        self.__get_pulse_width()
        self._duty_cycle = self.__get_duty_cycle()
        self._pwm.ChangeDutyCycle(self._duty_cycle)
        time.sleep(self._pulse_width / 1000)

    def write_duty_cycle(self, duty_cycle):

        self._pwm.ChangeDutyCycle(duty_cycle)

    def read_angle(self):

        return self._angle

    def __configure_pwm(self):

        self._pwm = GPIO.PWM(self._pin, self.s_model.frequency)
        self._pwm.start(self._duty_cycle)

    def __configure_pin(self, rasp_pin):

        self._pin = rasp_pin
        GPIO.setup(self._pin, GPIO.OUT)

    def __get_pulse_width(self):

        self._pulse_width = self.s_model.m_pulse * self._angle + self.s_model.n_pulse

    def __get_duty_cycle(self):

        return self._pulse_width * self.s_model.frequency / 10.0


if __name__ == "__main__":

    newservo = Servo(1)
    print("frequency: ", newservo.s_model.frequency)
    print("m_pulse: ", newservo.s_model.m_pulse)
    print("n_pulse: ", newservo.s_model.n_pulse)
    print("Duty Cycle: ", newservo.write_angle(10))
