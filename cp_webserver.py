# -*- coding: utf-8 -*-
# installer bottle biblioteket med 'pip install bottle' i shell
from bottle import route, run, template

import os     # Bibliotek til læs og skriv til filer
import glob   # Bibliptek til at søge i sti og filnavne
import re     # Regulær udtryk, vil du være 1337 h4ck3r så lær re.
import RPi.GPIO as GPIO   # Phyton bibliotek indeholde GPIO funktioner

GPIO.setmode(GPIO.BCM)    # Sæt BCM (broadcom layout) på Pins.
GPIO.setup(18, GPIO.OUT)  # Fortæl Raspberry at Pin 18 er en output Pin.

@route('/led/<parm>')
def index(parm):
    led_on = int(parm)
    GPIO.output(18, led_on)
    return template('<b>Led on {{parm}}</b>', parm=parm)

def get_temperatur():
    # åben termostat fil og læs data ind i variablen 'linier'
    termostat_fil = glob.glob('/sys/bus/w1/devices/28*')[0] + '/w1_slave'
    f = open(termostat_fil, 'r')
    linier = f.readlines()
    f.close()

    # Brug regulært udtryk til at finde temperaturen i linie 2 i læste fil.
    match = re.search(r't=([0-9]{5})', linier[1])
    temperatur = match.group(1)
    # Temperaturen er i tusinde del grader, så vi dividere med 1000 for at
    # udregne temperaturen i grader.
    temperatur = float(temperatur) / 1000

    return temperatur

@route('/temp')
def index():
    temperatur = get_temperatur()
    return template('<b>Temperaturen er {{t}} grader cencius</b>', t=temperatur)


#run(host='localhost', port=8080) # ikke synlig externt.
run(host='0.0.0.0', port=8080)    # OBS! Kører på phyton dev web server som ikke er sikker
GPIO.cleanup()
print('Bye-bye!')


