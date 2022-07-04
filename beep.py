import RPi.GPIO as GPIO
import time


def setup(pin, limit):
    pass
    GPIO.setmode(GPIO.BOARD)
    beep = pin

    GPIO.setup(beep, GPIO.OUT)

    global pwm
    pwm = GPIO.PWM(beep, limit)
    # pwm.ChangeDutyCycle(limit)
    pwm.start(0)


if __name__ == "__main__":
    pin = 11
    limit = 100
    setup(pin, limit)

    try:
        while True:
            pwm.ChangeDutyCycle(100)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    GPIO.cleanup()
