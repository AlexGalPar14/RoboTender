"""
Antes de ejecutar este test se debe comprobar la posición del soporte de vaso,
ya que si se mueve en la dirección errónea, el soporte de vaso puede llegar al final
del recorrido y romperse.
Se debe vigilar la dirección de giro del motor, si usar CW o CCW.
Se debe comprobar la cantidad de pasos (SPR).
29000: posición inicial a primera válvula
42000: posición inicial a segunda válvula
54000: posición inicial a tercera válvula
"""


import RPi.GPIO as GPIO
from time import sleep

# Configuración de los pines del motor
DIR = 21   # Pin para la dirección del motor
STEP = 20  # Pin para el paso del motor
CW = 1     # Dirección en sentido de las agujas del reloj (Clockwise)
CCW = 0    # Dirección en sentido contrario a las agujas del reloj (Counter-Clockwise)
SPR = 29000  # Pasos por revolución del motor (Step Per Revolution)

# Configuración de la Raspberry Pi
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

step_count = SPR
delay = 0.0003

for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)
GPIO.cleanup()
