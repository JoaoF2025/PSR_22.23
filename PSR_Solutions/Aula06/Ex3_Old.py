#!/usr/bin/env python3
#Test examples for Exercise 3

import numpy as np
import cv2


def main():
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    mouthCascade=cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
    capture = cv2.VideoCapture(0)
    alpha=0.2

    while True:

        _, img = capture.read()
        img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        output=img.copy()

        faces = faceCascade.detectMultiScale(
            gray,     
            scaleFactor=1.1,
            minNeighbors=6,     
            minSize=(60,60)
        )
        
        mouths = mouthCascade.detectMultiScale(
            gray, 
            scaleFactor=1.2, 
            minNeighbors=24,
            minSize=(40,40)
        )

        #Faces
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),-1)
            cv2.addWeighted(img, alpha, output, 1 - alpha, 0, output)
            cv2.rectangle(output,(x,y),(x+w,y+h),(0,255,0),3)

            #only shows mouth if it's on the bottom half of the face
            for (x,y,w,h) in mouths:
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), -1)
                cv2.addWeighted(img, alpha, output, 1 - alpha, 0, output)
                cv2.rectangle(output,(x,y),(x+w,y+h),(0,0,255),3)
       



        cv2.imshow('video',output)
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()