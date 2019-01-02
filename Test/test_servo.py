from unittest import TestCase
from servopi.Servo import Servo


class TestServo(TestCase):

    def setUp(self):
        self.servo = Servo(1, "sg90")

    def test_write_angle(self):

        self.servo.write_angle(90)

        self.assertEqual(1.5, self.servo._pulse_width)
        self.assertEqual(7.5, self.servo._duty_cycle)

    def test_write_duty_cycle(self):
        self.servo.write_duty_cycle(5)

        self.assertEqual(5, self.servo._duty_cycle)

    def test_read_angle(self):
        self.servo.write_angle(90)
        actual_angle = self.servo.read_angle()

        self.assertEqual(90, actual_angle)

    def test_read_duty_cycle(self):
        self.servo.write_duty_cycle(10)
        actual_duty_cycle = self.servo.read_duty_cycle()

        self.assertEqual(10, actual_duty_cycle)

