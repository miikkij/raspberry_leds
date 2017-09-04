from gpiozero import PWMLED
from time import sleep
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    green = PWMLED(47, active_high=False)

while True:
    for i in range(11):
        green.value = i / 10
        sleep(0.05)
    for i in reversed(range(11)):
        green.value = i / 10
        sleep(0.05)

