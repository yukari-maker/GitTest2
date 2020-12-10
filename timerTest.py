import time
from time import sleep
from adc_8chan_12bit import Pi_hat_adc
from time import perf_counter

start_time = 0.0

adc = Pi_hat_adc()

def timer():
    if adc.get_nchan_adc_raw_data(0) > 500:
        global start_time#正確かどうか見る
        start_time = perf_counter()
        print("started")
        sec = 0 #このまま使うとここでカウントリセットされる
        for sec in range(10):
            sec = sec + 1
            time.sleep(1)

        stop_time = perf_counter()
        end_time =(stop_time-start_time)
        print(end_time)
        print(sec)
def main_loop():
    while True:
        timer()
if __name__ == '__main__':
    main_loop()
