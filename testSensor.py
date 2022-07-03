import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

pin = 32

if __name__ == "__main__":
    GPIO.setup(pin, GPIO.IN)
    try:
        while True:
            if GPIO.input(pin) == GPIO.LOW:
                print("low...")
            if GPIO.input(pin) == GPIO.HIGH:
                print("high...")
            # time.sleep(1)
            # GPIO.output(led1, GPIO.LOW)
            # time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    GPIO.cleanup()
