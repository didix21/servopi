=======
servopi
=======
|build-status|

.. contents:: Table of Contents

Overview
========
This Python package contains a tool that allows to control servo motors in raspberry pi.
You can define a servo motor in a easy way without worrying about setting the raspberry pi PWM.
Moreover, you can move your servo motor using angles.

Features
========
- Set a servo pin.
- Move using angles.
- Move using duty cycle.

Installation
============

.. code:: bash

    $ pip install servopi

Examples
========

Example 1
---------
Define a SG90 servo model.

.. code:: Python

    from servopi import Servo


    def main():

        GPIO.setmode(GPIO.BOARD)
        angle = 120
        my_servo = Servo(11, "Sg90")
        my_servo.write_angle(angle)
        print("Moving: ", angle)


    if __name__ == "__main__":

        main()

Example 2
---------

.. code:: Python

    from servopi import Servo


    angle = 120
    rasberry_pin = 11
    frequency = 50
    max_angle = 180
    min_pulse_width = 0.5


    def main():

        GPIO.setmode(GPIO.BOARD)

        my_servo = Servo(11, "myown", (frequency, max_angle, min_pulse_width))
        my_servo.write_angle(angle)
        print("Moving: ", angle)


    if __name__ == "__main__":

        main()

.. |build-status| image:: https://travis-ci.org/didix21/mdutils.svg?branch=master
    :target: https://travis-ci.org/didix21/mdutils
    :alt: Build status
