from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep
import time
b = TonalBuzzer(17)
sec = 0 #このまま使うとここでカウントリセットされる

for sec in range(10):
    sec = sec + 1
    time.sleep(1)
    print(sec)
b.play(Tone(600))
sleep(3)
b.stop()