import time
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from gpiozero import LED
from time import sleep
from adc_8chan_12bit import Pi_hat_adc
from time import perf_counter

start_time = 0.0

adc = Pi_hat_adc()

b = TonalBuzzer(17)
led_a = LED(22)
led_b = LED(27)
sec = 0

def Buzzer():
    b.play(Tone(600))
    led_a.on()
    led_b.on()

def timer():
    if adc.get_nchan_adc_raw_data(0) > 500:

        print("started")
     #   sec = 0 #このまま使うとここでカウントリセットされる
        for sec in range(10):
         if adc.get_nchan_adc_raw_data(0) > 500:
             sec = sec + 1
             time.sleep(1)
        if adc.get_nchan_adc_raw_data(0) > 500:
            Buzzer()
        else:
            led_a.off()
            led_b.off()
            b.stop()
def main_loop():
    while True:
        timer()
if __name__ == '__main__':
    main_loop()
