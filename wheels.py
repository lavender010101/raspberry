import RPi.GPIO as GPIO
import time

PIN_IN1_L = 11
PIN_IN2_L = 12

PIN_IN1_R = 15
PIN_IN2_R = 13


def forward():
    GPIO.output(self.PIN_IN1_L, GPIO.HIGH)
    GPIO.output(self.PIN_IN2_L, GPIO.LOW)
    GPIO.output(self.PIN_IN1_R, GPIO.HIGH)
    GPIO.output(self.PIN_IN2_R, GPIO.LOW)


if __name__ == "__main__":
    try:
        while True:
            forward()
    except KeyboardInterrupt:
        print("Interrupted by keyboard.")
    GPIO.cleanup()
