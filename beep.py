import RPi.GPIO as GPIO
import time


def setup(pin):
    pass
    GPIO.setmode(GPIO.BOARD)
    beep = pin

    GPIO.setup(beep, GPIO.OUT)

    pwm = GPIO.PWM(beep)
    # pwm.ChangeDutyCycle(limit)
    pwm.start(0)


if __name__ == "__main__":
    pin = 11
    setup(pin)

    GPIO.PWM(pin).ChangeDutyCycle(100)
