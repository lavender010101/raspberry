# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO  #导入RPi.GPIO库

import time  #导入time库

GPIO.setmode(GPIO.BOARD)

pin21 = 21  #接声音传感器
GPIO.setup(pin21, GPIO.IN)  #设置引脚为输入模式
# GPIO.setup(pin21, GPIO.IN)  #设置引脚为输入模式

while True:

    # if GPIO.input(pin) == GPIO.LOW:  #有声音
    #     print("low")
    # else:
    #     print("high")

    print(GPIO.input(pin21))
    # print("pin21 -> " + GPIO.input(pin21))

    time.sleep(2)  #一秒一次
