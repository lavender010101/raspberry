# import action

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pin = 1
GPIO.setup(pin, GPIO.IN)
while True:
    if GPIO.input(pin) == GPIO.LOW:
        print("low")
    time.sleep(1000)
