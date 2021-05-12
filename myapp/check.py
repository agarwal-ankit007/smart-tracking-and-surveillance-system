import face_recognition
import cv2
import numpy as np
import os
from time import sleep
from camera import Face_Recog, object

initial_count = 0
for path in os.listdir("C:/Users/vivek/PycharmProjects/webapp/media"):
    initial_count += 1

def check_status():
    while True:
        count = 0
        for path in os.listdir("C:/Users/vivek/PycharmProjects/webapp/media"):
            count += 1
        global initial_count
        if count != initial_count:
            Face_Recog.encoding(object)
            initial_count = count
        print(count)
        sleep(5)

check_status()
