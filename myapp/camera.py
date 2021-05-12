import cv2,os,urllib.request
import numpy as np
from django.conf import settings
import face_recognition
from time import sleep
#from check import initial_count as ic

# face_detection_videocam = cv2.CascadeClassifier(os.path.join(
#     settings.BASE_DIR,'opencv_haarcascade_data/haarcascade_frontalface_default.xml'
# ))
#
# face_detection_webcam = cv2.CascadeClassifier(os.path.join(
#     settings.BASE_DIR,'opencv_haarcascade_data/haarcascade_frontalface_default.xml'
# ))

KNOWN_FACES_DIR = "C:/Users/vivek/PycharmProjects/webapp/media"
TOLERANCE = 0.6
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "cnn"

known_faces = []
known_names = []

initial_count = 0
for path in os.listdir(KNOWN_FACES_DIR):
    initial_count += 1
flag=True

class Face_Recog(object):
    # def _init_(self):
    #     self.video = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    # def _del_(self):
    #     self.video.release()
    def check_status(self):
        count = 0
        for path in os.listdir("C:/Users/vivek/PycharmProjects/webapp/media"):
            count += 1
        global initial_count
        if count != initial_count:
            self.encoding()
            initial_count = count
        print(count)

    def encoding(self):
        print("start")
        temp_faces = []
        temp_names = []
        for name in os.listdir(KNOWN_FACES_DIR):
            for filename in os.listdir('{}/{}'.format(KNOWN_FACES_DIR, name)):
                image = face_recognition.load_image_file('{}/{}/{}'.format(KNOWN_FACES_DIR, name, filename))
                encoding = face_recognition.face_encodings(image)[0]
                temp_faces.append(encoding)
                temp_names.append(name)
        global known_faces
        known_faces = temp_faces
        global known_names
        known_names = temp_names
        #return ("loaded")
        print(known_names)



    def test_func(self):
        #encoding
        self.video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True

        while True:
            global flag
            flag= flag+ 1
            if flag==5:
                self.check_status()
                flag=0
            # Grab a single frame of video
            global known_names
            global known_faces
            ret, frame = self.video.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Only process every other frame of video to save time
            if process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
                    name = "Unknown"

                    face_distances = face_recognition.face_distance(known_faces, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = known_names[best_match_index]
                        print("match found : {}".format(name))
                    else:
                        print("not found")
                    face_names.append(name)

            process_this_frame = not process_this_frame

            # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Display the resulting image
            cv2.imshow('Video', frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.video.release()
        cv2.destroyAllWindows()
        #return ("success")


object=Face_Recog()
#check_status(object)
object.encoding()
object.test_func()
