# -*- coding: utf-8 -*-

# Codingpriates Herning
# Eksempel 2 : Læs temperatur fra w-1 bus
# skriv temperatur up i consol

# Forudsætininger
# w-1 bus skal være slået til i interfaces (sudo raspi-config)
# DS18B20 termometer koblet til raspberry pin 4 (w-1 bus)

import os     # Bibliotek til læs og skriv til filer
import glob   # Bibliptek til at søge i sti og filnavne
import re     # Regulær udtryk, vil du være 1337 h4ck3r så lær re.

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

# Print den læste temperatur ud i consollen
print('Temperaturen er {0} grader cencius'.format(temperatur))


