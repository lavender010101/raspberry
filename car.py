import RPi.GPIO as GPIO
import time

PIN_IN1_L = 11
PIN_IN2_L = 12
PIN_IN1_R = 15
PIN_IN2_R = 16


class Car:

    def __init__(self, PIN_IN1_L, PIN_IN2_L, PIN_IN1_R, PIN_IN2_R):
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)

        self.PIN_IN1_L = PIN_IN1_L
        self.PIN_IN2_L = PIN_IN2_L
        self.PIN_IN1_R = PIN_IN1_R
        self.PIN_IN2_R = PIN_IN2_R

        GPIO.setup(self.PIN_IN1_L, GPIO.OUT)
        GPIO.setup(self.PIN_IN2_R, GPIO.OUT)
        GPIO.setup(self.PIN_IN1_R, GPIO.OUT)
        GPIO.setup(self.PIN_IN2_R, GPIO.OUT)

    def forward(self):
        GPIO.output(self.PIN_IN1_L, GPIO.HIGH)
        GPIO.output(self.PIN_IN2_L, GPIO.LOW)
        GPIO.output(self.PIN_IN1_R, GPIO.HIGH)
        GPIO.output(self.PIN_IN2_R, GPIO.LOW)

    def backward(self):
        GPIO.output(self.PIN_IN1_L, GPIO.LOW)
        GPIO.output(self.PIN_IN2_L, GPIO.HIGH)
        GPIO.output(self.PIN_IN1_R, GPIO.LOW)
        GPIO.output(self.PIN_IN2_R, GPIO.HIGH)

    def turn_left(self):
        GPIO.output(self.PIN_IN1_L, GPIO.HIGH)
        GPIO.output(self.PIN_IN2_L, GPIO.LOW)
        GPIO.output(self.PIN_IN1_R, GPIO.LOW)
        GPIO.output(self.PIN_IN2_R, GPIO.LOW)

    def turn_right(self):
        GPIO.output(self.PIN_IN1_L, GPIO.LOW)
        GPIO.output(self.PIN_IN2_L, GPIO.LOW)
        GPIO.output(self.PIN_IN1_R, GPIO.HIGH)
        GPIO.output(self.PIN_IN2_R, GPIO.LOW)

    def stop(self):
        GPIO.output(self.PIN_IN1_L, GPIO.LOW)
        GPIO.output(self.PIN_IN2_L, GPIO.LOW)
        GPIO.output(self.PIN_IN1_R, GPIO.HIGH)
        GPIO.output(self.PIN_IN2_R, GPIO.LOW)


if __name__ == "__main__":
    try:
        car = Car(PIN_IN1_L, PIN_IN2_L, PIN_IN1_R, PIN_IN2_R)

        car.forward()
        time.sleep(5)
        car.stop()
        time.sleep(1)

    except KeyboardInterrupt:
        print("Interrupted by keyboard.")
        GPIO.cleanup()
