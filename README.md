# Raspberry PI Leds
Python scripts to control Raspberry Pi's LEDs. 

## Note!
Currently scripts only work well on Raspberry Pi Zero W

# Install
sudo apt install python-gpiozero

# Testing
python pi_zero_w.py

# As a service
Soon.

# Control through file system
One signal at a time. Create file to /tmp/signal[n] 
```touch /tmp/signal1```
and just remove if you want to reset signal
```rm /tmp/signal1```


