# Python
#
# This file only is needed for developing servopi package.
#
# This file is part of servopi: https://github.com/didix21/servopi
#
# MIT License: (C) 2018 Dídac Coll


# Constants

OUT = 1

# Methods


class PWM(object):

    def __init__(self, channel, frequency):

        print("PWM Pin: ", channel)
        print("PWM Frequency: ", frequency)

    @staticmethod
    def start(duty_cycle):

        print("PWM.start Duty Cycle: ", duty_cycle)

    @staticmethod
    def ChangeDutyCycle(duty_cycle):

        print("PWM.ChangeDutyCycle Duty Cicle: ", duty_cycle)


def setup(channel, mode):

    print("setup Pin: ", channel)
    print("setup Mode: ", mode)


def cleanup(channels=[]):

    print("cleanup pins: ", channels)


if __name__ == "__main__":

    PWM(1, 50)
    setup(2, OUT)
    cleanup([1, 2, 3, 4])
    cleanup()
    pwm = PWM(1, 50)
    pwm.start(5)
    pwm.ChangeDutyCycle(10)
