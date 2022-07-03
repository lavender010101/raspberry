# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO  #导入RPi.GPIO库

import time  #导入time库

pin = 17  #接声音传感器

GPIO.setmode(GPIO.BCM)  #设置引脚为BCM

GPIO.setup(pin, GPIO.IN)  #设置引脚为输入模式

while True:

    if GPIO.input(pin) == GPIO.LOW:  #有声音
        print("low")
    else:
        print("high")

    time.sleep(2)  #一秒一次
