import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

btn = 35
led1 = 29
led2 = 31


def switchy(flag):
    if flag == 0:
        GPIO.output(led1, GPIO.LOW)
        GPIO.output(led2, GPIO.LOW)
    if flag % 2 == 1:
        GPIO.output(led1, GPIO.HIGH)
        GPIO.output(led2, GPIO.LOW)
    elif flag % 2 == 0:
        GPIO.output(led1, GPIO.LOW)
        GPIO.output(led2, GPIO.HIGH)


if __name__ == "__main__":
    GPIO.setup(btn, GPIO.IN)
    GPIO.setup(led1, GPIO.OUT)
    GPIO.setup(led2, GPIO.OUT)

    try:
        flag = 0
        while True:
            switchy(flag)
            if GPIO.input(btn) == GPIO.HIGH:
                flag += 1
                switchy(flag)
                time.sleep(1)

    except KeyboardInterrupt:
        print("Exiting...")
    GPIO.cleanup()
