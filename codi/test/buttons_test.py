"""
Test que comprueba el funcionamiento de los 3 botones.
Cuando se presiona un botón, sale un mensaje por terminal que dice el número del que ha sido presionado.
"""

import RPi.GPIO as GPIO
import time

# Configura los pines de los botones
PIN_BUTTON_1 = 23
PIN_BUTTON_2 = 24
PIN_BUTTON_3 = 25

# Configura la biblioteca GPIO para usar la numeración de los pines de la placa
GPIO.setmode(GPIO.BCM)

# Configura los pines de los botones como entrada con resistencia pull-up
GPIO.setup(PIN_BUTTON_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_BUTTON_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_BUTTON_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def esperar_boton():
    while True:
        # Comprueba si se ha presionado el botón 1
        if not GPIO.input(PIN_BUTTON_1):
            print("Presionado botón 1")
            # Espera un segundo para evitar múltiples detecciones de un solo pulsado
            time.sleep(0.5)
        # Comprueba si se ha presionado el botón 2
        elif not GPIO.input(PIN_BUTTON_2):
            print("Presionado botón 2")
            time.sleep(0.5)
        # Comprueba si se ha presionado el botón 3
        elif not GPIO.input(PIN_BUTTON_3):
            print("Presionado botón 3")
            time.sleep(0.5)

try:
    # Espera a que se presione un botón
    esperar_boton()
except KeyboardInterrupt:
    print("\nPrograma terminado por el usuario.")
finally:
    # Limpia la configuración de los pines GPIO antes de salir
    GPIO.cleanup()
