# import action

import RPi.GPIO as GPIO
import time

pin = 1
GPIO.setup(pin, GPIO.IN)
while True:
    if GPIO.input(pin) == GPIO.LOW:
        print("low")
    time.sleep(1000)
