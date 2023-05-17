import cv2
import picamera
import picamera.array
import time

# Iniciar la cámara
camera = picamera.PiCamera()

# Configurar la resolución y la velocidad de fotogramas
camera.resolution = (640, 480)
camera.framerate = 30

# Crear un objeto de arreglo para capturar la imagen
stream = picamera.array.PiRGBArray(camera, size=(640, 480))

# Permitir que la cámara se caliente
time.sleep(2)

# Iniciar el bucle principal
for frame in camera.capture_continuous(stream, format="bgr", use_video_port=True):
    image = frame.array
    cv2.imshow("Cámara", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    stream.truncate(0)

camera.close()
cv2.destroyAllWindows()
