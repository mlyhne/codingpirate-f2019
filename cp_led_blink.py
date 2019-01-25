# -*- coding: utf-8 -*-

# Codingpriates Herning
# Eksempel 1 : Tænd og sluk lysdiode

import RPi.GPIO as GPIO   # Phyton bibliotek indeholde GPIO funktioner
import time               # Phyton bibliotek indeholde sleep funtionen

GPIO.setmode(GPIO.BCM)    # Sæt BCM (broadcom layout) på Pins.
GPIO.setup(18, GPIO.OUT)  # Fortæl Raspberry at Pin 18 er en output Pin.

try:
    while True:
        GPIO.output(18,1) # Tænd lysdiode på Pin 18
        time.sleep(2)     # vent i 2 sekunder.
        GPIO.output(18,0) # Sluk lysdiode på Pin 18
        time.sleep(2)     # vent i 2 sekunder.
except KeyboardInterrupt: # Keyboard Crtl-C (stop program)
    GPIO.cleanup()        # nulstil alle GPIO pins
    print("Keyboard Interrupt, cleanup and stop program")
    


