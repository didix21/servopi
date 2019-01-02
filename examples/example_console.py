import RPi.GPIO as GPIO
from servopi.Servo import Servo


def main():

    GPIO.setmode(GPIO.BOARD)
    raspberry_pin = 11
    my_servo = Servo(raspberry_pin)

    while True:

        angle = input("Write an angle: ")
        my_servo.write_angle(int(angle))

        duty_cycle = input("Write duty cycle: ")
        my_servo.write_duty_cycle(float(duty_cycle))


if __name__ == "__main__":

    main()
