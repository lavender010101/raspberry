import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

btn = 35

if __name__ == "__main__":
    GPIO.setup(btn, GPIO.IN)

    try:
        while True:
            if GPIO.input(btn) == GPIO.LOW:
                print("low...")
            if GPIO.input(btn) == GPIO.HIGH:
                print("high...")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    GPIO.cleanup()
