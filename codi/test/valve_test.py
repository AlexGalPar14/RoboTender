"""
Test que abre la válvula durante 5 segundos y la cierra durante otros 5 segundos.
"""

from gpiozero import LED
from time import sleep

VALVE_PIN = 2

valve = LED(VALVE_PIN)
while True:
    valve.on()
    sleep(5)
    valve.off()
    sleep(5)
    print(valve.value)