#-*- coding: utf-8 -*
import RPi.GPIO as GPIO
import time

# 设置引脚编号模式
GPIO.setmode(GPIO.BOARD)


class Buzzer_Song(object):
    # pin_buzzer是IO引脚， delay_beat是一个音持续的时间（节拍时长控制）
    def __init__(self, pin_buzzer, pin_btn, delay_beat=0.5):
        # 设置蜂鸣器引脚模式
        self.pin_buzzer = pin_buzzer
        self.pin_btn = pin_btn
        GPIO.setup(self.pin_buzzer, GPIO.OUT)
        GPIO.setup(self.pin_btn, GPIO.IN)
        # 创建PWM对象初始频率 440hz，占空比50%
        self.Buzzer = GPIO.PWM(pin_buzzer, 440)
        self.Buzzer.start(50)
        # 音符到频率的转换字典，cl低音，cm中音，ch高音
        self.note2freq = {
            "cl1": 131,
            "cl2": 147,
            'cl3': 165,
            "cl4": 175,
            "cl5": 196,
            "cl6": 211,
            "cl7": 248,
            "cm1": 262,
            "cm2": 294,
            'cm3': 330,
            "cm4": 350,
            "cm5": 393,
            "cm6": 441,
            "cm7": 495,
            "ch1": 525,
            "ch2": 589,
            'ch3': 661,
            "ch4": 700,
            "ch5": 786,
            "ch6": 882,
            "ch7": 990
        }
        # 节拍时长初始化
        self.delay_beat = delay_beat

    def play_song(self, notes, beats):
        for note, beat in zip(notes, beats):
            # 切换频率，演奏音乐
            self.Buzzer.ChangeFrequency(self.note2freq[note])
            # 持续的时间
            # time.sleep(self.delay_beat * beat)
            delay_time = self.delay_beat * beat / 0.01
            self.action(delay_time)

    def action(self, delay_time):
        cnt = 0

        # delay
        while delay_time > 0:
            if GPIO.input(self.pin_btn) == GPIO.HIGH:
                cnt += 1
            time.sleep(0.01)
            delay_time -= 1
        # start
        if cnt == 1:
            return 1
        # exit
        elif cnt >= 3:
            self.destroy()
            return 3
        # stop
        elif cnt == 2:
            return 2
        return 0

    # 对象销毁
    def destroy(self):
        self.Buzzer.stop()
        GPIO.output(self.pin_buzzer, GPIO.LOW)
        GPIO.cleanup()


if __name__ == "__main__":
    # 定义buzzer引脚
    pin_buzzer = 11
    pin_btn = 35
    # 定义一个对象 m_buzzer_song
    m_buzzer_song = Buzzer_Song(pin_buzzer, pin_btn, 0.3)
    notes = [
        'cm1', 'cm1', 'cm1', 'cl5', 'cm3', 'cm3', 'cm3', 'cm1', 'cm1', 'cm3',
        'cm5', 'cm5', 'cm4', 'cm3', 'cm2', 'cm2', 'cm3', 'cm4', 'cm4', 'cm3',
        'cm2', 'cm3', 'cm1', 'cm1', 'cm3', 'cm2', 'cl5', 'cl7', 'cm2', 'cm1'
    ]
    beats = [
        1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 3, 1, 1, 2, 2, 1, 1, 2, 2, 1,
        1, 2, 2, 1, 1, 3
    ]
    # 循环演奏音乐
    try:
        while True:
            start = 0
            while start < 1:
                start = m_buzzer_song.action(1)
            m_buzzer_song.play_song(notes, beats)
    except KeyboardInterrupt:
        print('\n Ctrl + C QUIT')
    finally:
        m_buzzer_song.destroy()
