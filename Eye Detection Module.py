import numpy
import cv2
import time
from playsound import playsound

eye_cascPath = 'D:/iiit/pis/haarcascade_eye_tree_eyeglasses.xml'  #eye detect model
face_cascPath = 'C:\\Users\\Avinoor\\haarcascade_frontalface_default.xml'  #face detect model
faceCascade = cv2.CascadeClassifier(face_cascPath)
eyeCascade = cv2.CascadeClassifier(eye_cascPath)
count=0
cap = cv2.VideoCapture(0)
while 1:

    ret, img = cap.read()
    if ret:
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            frame,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            # flags = cv2.CV_HAAR_SCALE_IMAGE
        )
        # print("Found {0} faces!".format(len(faces)))
        if len(faces) > 0:
            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            frame_tmp = img[faces[0][1]:faces[0][1] + faces[0][3], faces[0][0]:faces[0][0] + faces[0][2]:1, :]
            frame = frame[faces[0][1]:faces[0][1] + faces[0][3], faces[0][0]:faces[0][0] + faces[0][2]:1]
            eyes = eyeCascade.detectMultiScale(
                frame,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                # flags = cv2.CV_HAAR_SCALE_IMAGE
            )
            
            if len(eyes) == 0:
         
            	count=count+0.5
            	if count==6:

            		count=0
            		playsound('alarm.mp3')
            else:
                count=0
            frame_tmp = cv2.resize(frame_tmp, (800, 800), interpolation=cv2.INTER_LINEAR)
            cv2.imshow('Face Recognition', frame_tmp)
        waitkey = cv2.waitKey(1)
        if waitkey == ord('q') or waitkey == ord('Q'):
            cv2.destroyAllWindows()
            break
