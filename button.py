import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

btn = 35
led1 = 29
led2 = 31


def switchy(flag):
    if flag == 1:
        GPIO.output(led1, GPIO.HIGH)
        GPIO.output(led2, GPIO.LOW)
    elif flag == 2:
        GPIO.output(led1, GPIO.LOW)
        GPIO.output(led2, GPIO.HIGH)
    elif flag == 0:
        GPIO.output(led1, GPIO.LOW)
        GPIO.output(led2, GPIO.LOW)


if __name__ == "__main__":
    GPIO.setup(btn, GPIO.IN)
    GPIO.setup(led1, GPIO.OUT)
    GPIO.setup(led2, GPIO.OUT)

    try:
        flag = 0
        while flag < 2:
            switchy(flag)
            if GPIO.input(btn) == GPIO.HIGH:
                time.sleep(1)
                flag += 1

    except KeyboardInterrupt:
        print("Exiting...")
    GPIO.cleanup()
