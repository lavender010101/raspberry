# import action

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pin = 1
GPIO.setup(pin, GPIO.IN)
while True:
    if GPIO.input(pin, True):
        print("true")
    time.sleep(1000)
