import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

led1 = 21
# led2 = 5

if __name__ == "__main__":
    GPIO.setup(led1, GPIO.OUT)

    try:
        while True:
            GPIO.output(led1, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(led1, GPIO.LOW)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    GPIO.cleanup()
