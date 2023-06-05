import face_recognition
import numpy as np
import os
import threading
import cv2
import time
import glob

class FaceRecognitionModule():

    def __init__(self, **kwargs):
        self.frames = []
        self.result = {}
        self.is_running = False
        self.thread = None
        self._stop = threading.Event()

        self.known_face_encodings = []
        self.known_face_names = []
        self.face_recognition = None
        self.save_path = kwargs.get('save_path', 'data/face')
    
    def load_model(self) -> None:
        self.face_recognition = face_recognition
    
    def unload_model(self) -> None:
        self.face_recognition = None
    
    def add_frame(self, frame) -> None:
        '''
        Esta función se llama cuando se quiere agregar un frame al módulo. El frame es una imagen
        en formato numpy.ndarray (Leido con cv2.imread()). El frame es una imagen en formato BGR.
        '''
        self.frames.append(frame)
    
    def del_frames(self) -> None:
        '''
        Esta función se llama cuando se quiere eliminar los frames que se agregaron al módulo.
        '''
        self.frames = []
    
    def run_inferece(self) -> None:
        '''
        Esta función se llama cuando se quiere ejecutar la inferencia del módulo. Se tiene que ejecutar
        en segundo plano, es decir, no se tiene que bloquear el hilo principal con el uso de un thread.
        '''
        self.is_running = True
        self.thread = threading.Thread(target=self._run_inferece)
        self.thread.start()
    
    def get_result(self) -> dict:
        """This function is called when the module wants to get the result of the inference.

        Returns:
            dict: { Name: [name1, name2, name3...], Face: [face1, face2, face3...], Encoding: [encoding1, encoding2, encoding3...] }
        """
        return self.result

    def kill_inferece(self):
        '''
        Esta función se llama cuando se quiere matar la inferencia del módulo.
        '''
        self.is_running = False
        self._stop.set()
    
    def is_finished(self):
        '''
        Esta función se llama para saber si el módulo terminó de procesar el frame/frames actuales.
        '''
        return not self.is_running
    
    def _run_inferece(self) -> None:
        self.load_db()
        unknown_detected = 0
        threshold = 0.5
        self.result = {'names': [], 'faces': [], 'encodings': []}
        known_encodings = np.array(self.known_face_encodings)
        known_names = self.known_face_names

        for frame in self.frames:
            face_locations = self.face_recognition.face_locations(frame)
            faces_encondigs = self.face_recognition.face_encodings(frame, face_locations, model="large")

            for idx, face_encondig in enumerate(faces_encondigs):
                matches = self.face_recognition.compare_faces(known_encodings, face_encondig, threshold)
                face_distances = self.face_recognition.face_distance(known_encodings, face_encondig)
                best_match_index = np.argmin(face_distances)

                face = frame[face_locations[idx][0]:face_locations[idx][2], face_locations[idx][3]:face_locations[idx][1]]
                img_face = cv2.resize(face, (0, 0), fx=0.5, fy=0.5)

                if matches[best_match_index]:
                    name = known_names[best_match_index].replace("_", " ")
                    self.result['names'].append(name)
                    self.result['faces'].append(img_face)
                    self.result['encodings'].append(face_encondig)
                else:
                    unknown_encodings = np.array(self.result['encodings'])
                    unknown_names = np.array(self.result['names'])
                    unknown_distances = self.face_recognition.face_distance(unknown_encodings, face_encondig)

                    if len(unknown_names) > 0 and np.min(unknown_distances) <= threshold:
                        idx = np.argmin(unknown_distances)
                        self.result['names'].append(self.result['names'][idx])
                        self.result['faces'].append(img_face)
                        self.result['encodings'].append(face_encondig)
                    else:
                        unknown_detected += 1
                        self.result['names'].append(f'Unknown {unknown_detected}')
                        self.result['faces'].append(img_face)
                        self.result['encodings'].append(face_encondig)
            
        self.is_running = False

    def organize_unknowns_folder(self):
        unknown_face_encodings = []
        unknown_face_names = []
        known_face_encodings = []
        known_face_names = []

        for file_path in glob.glob(os.path.join(self.save_path, "Unknown", "**", "*.txt"), recursive=True):
            with open(file_path, 'r') as f:
                encoding = np.loadtxt(f)
            dir_name = os.path.basename(os.path.dirname(file_path))
            name_file = os.path.basename(file_path)[:-4]
            dir_name_file = dir_name + '/' + name_file

            if dir_name == "Unknown":
                unknown_face_encodings.append(encoding)
                unknown_face_names.append(dir_name_file)
            else:
                known_face_encodings.append(encoding)
                known_face_names.append(dir_name)

        for idx, unknown_face_encoding in enumerate(unknown_face_encodings):
            matches = self.face_recognition.compare_faces(known_face_encodings, unknown_face_encoding, 0.5)
            dir_name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                dir_name = known_face_names[first_match_index].split('/')[0]
                file_name = unknown_face_names[idx].split('/')[1]
                os.rename(f'{self.save_path}/{unknown_face_names[idx]}.txt', f'{self.save_path}/Unknown/{dir_name}/{file_name}.txt')
                os.rename(f'{self.save_path}/{unknown_face_names[idx]}.jpg', f'{self.save_path}/Unknown/{dir_name}/{file_name}.jpg')
            else:
                unknown_distances = self.face_recognition.face_distance(known_face_encodings, unknown_face_encoding)

                if len(unknown_distances) > 0 and np.min(unknown_distances) <= 0.5:
                    idx = np.argmin(unknown_distances)
                    dir_name = known_face_names[idx].split('/')[0]
                    file_name = unknown_face_names[idx].split('/')[1]
                    os.rename(f'{self.save_path}/{unknown_face_names[idx]}.txt', f'{self.save_path}/Unknown/{dir_name}/{file_name}.txt')
                    os.rename(f'{self.save_path}/{unknown_face_names[idx]}.jpg', f'{self.save_path}/Unknown/{dir_name}/{file_name}.jpg')
                else:
                    file_name = unknown_face_names[idx].split('/')[1]
                    dir_name = file_name
                    os.mkdir(f'{self.save_path}/Unknown/{file_name}')
                    os.rename(f'{self.save_path}/{unknown_face_names[idx]}.txt', f'{self.save_path}/Unknown/{file_name}/{file_name}.txt')
                    os.rename(f'{self.save_path}/{unknown_face_names[idx]}.jpg', f'{self.save_path}/Unknown/{file_name}/{file_name}.jpg')                
                    
            known_face_encodings.append(unknown_face_encoding)
            known_face_names.append(dir_name)

    def save_to_disk(self):
        for name, face, encoding in zip(self.result['names'], self.result['faces'], self.result['encodings']):
            if not "Unknown" in name: continue
            name = str(time.time()).replace(".", "_")
            with open(os.path.join(self.save_path, 'Unknown', name + '.txt'), 'w') as f:
                np.savetxt(f, encoding)
            cv2.imwrite(os.path.join(self.save_path, 'Unknown', name + '.jpg'), face)
                

    def load_db(self):
        self.known_face_encodings = []
        self.known_face_names = []

        for name in os.listdir(self.save_path):
            if name == "Unknown": continue
            for file in os.listdir(os.path.join(self.save_path, name)):
                if file.endswith(".txt"):
                    with open(os.path.join(self.save_path, name, file), 'r') as f:
                        self.known_face_encodings.append(np.loadtxt(f))
                    self.known_face_names.append(name)


    def generate_audio(self):
        if self.result['names'] == []:
            return "%modulo_caras_audio5%"
        resultado_txt = ""
        for name in list(set(self.result['names'])):
            resultado_txt += f"%modulo_caras_audio3% %modulo_caras_audio4% {name}, "
        return resultado_txt[:-2]

'''
# functions that maybe are not necessary
    def save_to_db(self):
        characteristics = self.take_pictures()
        name = input("Enter the full name of the person: ")
        name = name.replace(" ", "_")

        os.mkdir('face/db/' + name)
        os.mkdir('face/db/' + name)

        for i in range(len(characteristics)):
            np.savetxt('face/db/' + name + '/' + str(i) + '.txt', characteristics[i])

    def take_pictures(self):
        characteristics = []
        print("take face picture")
        input("press enter to take a picture")
        option = "y"
        while option != "n":
            self.camera.update()
            frame = self.camera.get_frame()
            face = self.face_recognition.face_locations(frame)
            if face != []:
                characteristics.append(self.face_recognition.face_encodings(frame, face, model="large"))
            option = input("Would you like take another? (y/n): ")
            
        return characteristics

    def learn_new_face(self):
        option = input("would you like to learn new face? (y/n): ")
        if option == "y":
            self.save_to_db()
'''
