from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from gpiozero import LED
from time import sleep
import time

b = TonalBuzzer(17)
led_a = LED(22)
led_b = LED(27)
sec = 0

def Buzzer():
    b.play(Tone(600))
    led_a.on()
    led_b.on()
    sleep(3)
    b.stop()

def BuzzerTimer():
    for sec in range(10):
        sec = sec + 1
        time.sleep(1)
        print(sec)
    Buzzer()

def main_loop():
    while True:
        BuzzerTimer()
if __name__ == '__main__':
    main_loop()
