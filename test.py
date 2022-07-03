import RPi.GPIO as GPIO  #导入库

pin = 1
GPIO.setmode(GPIO.BCM/BOARD)  # 引入针脚模式BMC或者BOARD模式

GPIO.setup(pin, GPIO.IN)  #设置引脚为输入

# GPIO.setup(pin, GPIO.OUT)  #设置引脚为输出
# 
# GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)  #设置初始化为高电平
# 
# GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)  #设置初始化为低电平
