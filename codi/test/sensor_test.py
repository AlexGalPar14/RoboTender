"""
Test que escribe por terminal cada segundo si está detectando un objeto el sensor o no.
"""

import RPi.GPIO as GPIO
import time

# Configurar el pin GPIO que utilizarás
PIN_SENSOR = 18

# Configurar el modo de numeración de pines y el pin como entrada
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_SENSOR, GPIO.IN)

def main():
    try:
        while True:
            # Leer el estado del sensor
            estado_sensor = GPIO.input(PIN_SENSOR)

            if estado_sensor == GPIO.HIGH:
                print("Objeto detectado!")
            else:
                print("No hay objeto")

            # Esperar un poco antes de leer el estado nuevamente
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Saliendo...")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
