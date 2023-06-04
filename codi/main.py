from face_recognition_module import FaceRecognitionModule
import cv2
from camera import Camera
import RPi.GPIO as GPIO
import time
import os
import shutil
from gpiozero import LED

camera = Camera()

face_recognition = FaceRecognitionModule()
face_recognition.load_model()

PIN_SENSOR = 18
PIN_VALVE = 2
PIN_BUTTON_1 = 23
PIN_BUTTON_2 = 24
PIN_BUTTON_3 = 25

PIN_MOTOR_DIR = 21
PIN_MOTOR_STEP = 20
clockWise = 1
counterClockWise = 0
stepRevolutionInitial = 29000
stepRevolutionSecond = 13000
stepRevolutionThird = 12000
motorStepDelay = 0.0003

valve = LED(PIN_VALVE)

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_SENSOR, GPIO.IN)

GPIO.setup(PIN_BUTTON_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_BUTTON_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_BUTTON_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_MOTOR_DIR, GPIO.OUT)
GPIO.setup(PIN_MOTOR_STEP, GPIO.OUT)


def select_beverage_buttons():
    while True:
        if not GPIO.input(PIN_BUTTON_1):
            return 1
        elif not GPIO.input(PIN_BUTTON_2):
            return 2
        elif not GPIO.input(PIN_BUTTON_3):
            return 3


def save_beverage(id):
    print('Introdueix la teva beguda preferida usant els botons')
    beverage_selected = select_beverage_buttons()
    directory_rute = os.path.join('data', 'face', 'user_' + str(id), 'beverage')
    os.makedirs(directory_rute, exist_ok=True)

    file_rute = os.path.join(directory_rute, 'user_' + str(id) + '.txt')

    with open(file_rute, "w") as archivo:
        archivo.write(str(beverage_selected))

    print(f"Beguda preferida guardada correctament")


def get_beverage(nameUser):
    file_rute = os.path.join('data', 'face', nameUser, 'beverage', nameUser + '.txt')
    try:
        with open(file_rute, "r") as file:
            numero = str(file.read().strip())
        return int(numero)
    except FileNotFoundError:
        print(f"L'arxiu {file_rute} no s'ha trobat")
        return None
    except ValueError:
        print(f"El continugt de l'arxiu {file_rute} no s'ha pogut llegir correctament")
        return None


def faces_rename():
    id = 1
    images_dir = os.path.join('data', 'face', 'Unknown')
    people = os.listdir(images_dir)

    # Si people és buit, vol dir que ha reconegut a una persona prèviament registrada al sistema
    if people:
        print("Registrant nou usuari")
        while True:
            if os.path.exists(os.path.join('data', 'face', 'user_' + str(id))):
                id = id + 1
            else:
                os.makedirs(os.path.join('data', 'face', 'user_' + str(id)))
                break

        old_dir = os.path.join('data', 'face', 'Unknown', people[0])
        new_dir = os.path.join('data', 'face', 'user_' + str(id))

        for file in os.listdir(old_dir):
            shutil.move(os.path.join(old_dir, file), new_dir)

        os.rmdir(old_dir)

        save_beverage(id)
        return 'user_' + str(id)
    else:
        return None


def fillCup(beverage):
    if beverage == 1:
        stepCount = stepRevolutionInitial
    elif beverage == 2:
        stepCount = stepRevolutionInitial + stepRevolutionSecond
    else:
        stepCount = stepRevolutionInitial + stepRevolutionSecond + stepRevolutionThird

    # Seqüència de moure got fins a la vàlvula seleccionada
    print('Iniciant moviment del got')
    GPIO.output(PIN_MOTOR_DIR, counterClockWise)
    for x in range(stepCount):
        GPIO.output(PIN_MOTOR_STEP, GPIO.HIGH)
        time.sleep(motorStepDelay)
        GPIO.output(PIN_MOTOR_STEP, GPIO.LOW)
        time.sleep(motorStepDelay)

    time.sleep(2)

    # Seqüència d'obertura de vàlvula
    print('S\'emplena el got')
    valve.on()
    time.sleep(20)
    valve.off()

    time.sleep(2)

    # Seqüència de volta al principi
    print('Retornant got a posició inicial')
    GPIO.output(PIN_MOTOR_DIR, clockWise)
    for x in range(stepCount):
        GPIO.output(PIN_MOTOR_STEP, GPIO.HIGH)
        time.sleep(motorStepDelay)
        GPIO.output(PIN_MOTOR_STEP, GPIO.LOW)
        time.sleep(motorStepDelay)


def facial_recognition():
    for i in range(3):
        print(f'frame {i}')
        camera.update()
        frame = camera.get_frame()
        face_recognition.add_frame(frame)

    face_recognition.run_inferece()

    while face_recognition.is_running:
        pass

    results = face_recognition.get_result()

    for name, face in zip(results['names'], results['faces']):
        nameUser = name.replace(" ", "_")
        cv2.imshow(name, face)
        cv2.destroyAllWindows()
    face_recognition.save_to_disk()
    face_recognition.organize_unknowns_folder()
    return nameUser


def bucle_principal():
    print("Bucle Principal Iniciat")
    nameUser = ''
    while True:
        print("Lectura de sensor")
        estado_sensor = GPIO.input(PIN_SENSOR)

        if estado_sensor == GPIO.HIGH:
            print("Objecte detectat: iniciant càmera")
            time.sleep(1)
            nameUser = facial_recognition()
            newUserName = faces_rename()
            beverage = None
            if newUserName is not None:
                newUserName = newUserName.replace(" ", "_")
                beverage = get_beverage(newUserName)
                fillCup(beverage)
            else:
                if nameUser:
                    beverage = get_beverage(nameUser)
                    fillCup(beverage)
                else:
                    print('Reconeixement facil fallit, torni a intentar-ho')

        time.sleep(1)


if __name__ == "__main__":
    bucle_principal()