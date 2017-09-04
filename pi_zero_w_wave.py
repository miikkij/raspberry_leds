from gpiozero import PWMLED
from time import sleep
import warnings
import os.path

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    green = PWMLED(47, active_high=False)

blinky_format = 0
blinky_step = 0

def check_blinky_format():
    """This function looks up for if signal files exist and sets LED Blinking Format"""
    global blinky_format
    global blinky_step
    if os.path.isfile("/tmp/signal1"):
        new_blinky_format = 1
    elif os.path.isfile("/tmp/signal2"):
        new_blinky_format = 2
    elif os.path.isfile("/tmp/signal3"):
        new_blinky_format = 3
    elif os.path.isfile("/tmp/signal4"):
        new_blinky_format = 4
    else: 
        new_blinky_format = 0
    if new_blinky_format != blinky_format: # If format has changed, then reset step state
        blinky_step = 0
        blinky_format = new_blinky_format

while True:
    check_blinky_format()
    print "blinky_format: ", blinky_format
    if blinky_format == 0: # Led is LID all the time
        green.value = 1;
        sleep(1)
    elif blinky_format == 1: # Gradually increase brightness
        blinky_step += 1
	if blinky_step > 100:  
            blinky_step = 1
        led_brightness = blinky_step / 100.0
        print led_brightness
        green.value = led_brightness
        sleep(0.01)
    elif blinky_format == 2: # Gradually lessen brightness
        blinky_step += 1
        if blinky_step > 100:
            blinky_step = 1;
        led_brightness = (101-blinky_step) / 100.0
        print led_brightness
        green.value = led_brightness
        sleep(0.01)
    elif blinky_format == 3: # Rapidly blink 0.1 sec pulse
        blinky_step += 1
        if blinky_step > 100:
            blinky_step = 0
        onoff = blinky_step%2
        print "onoff:", onoff, ":", onoff*1
        sleep(0.1)
        green.value = onoff * 1
    elif blinky_format == 4: # Blink for 0.1 sec after 0.5 sec of darkness 
        blinky_step += 1
        if blinky_step > 100:
            blinky_step = 0
        onoff = blinky_step % 2
        print "onoff:", onoff, ":", onoff*1
        if onoff==0:
            green.value = 0
            sleep(0.5)
        else:
            green.value = 1
            sleep(0.1)
    else: # Unknown blinky_format, put led 0.2 strength   
        green.value = 0.2
