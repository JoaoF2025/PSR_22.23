#!/usr/bin/env python3
#Test examples for Exercise 3

import numpy as np
import cv2


def main():
    faceCascade = cv2.CascadeClassifier('/home/joaof2025/PSR_22.23/PSR_Solutions/Aula06/haarcascade_frontalface_default.xml')
    capture = cv2.VideoCapture(0)
    alpha=0.2

    while True:

        _, img = capture.read()
        img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        output=img.copy()
        faces = faceCascade.detectMultiScale(
            gray,     
            scaleFactor=1.2,
            minNeighbors=5,     
            minSize=(30, 30)
        )
        
        #print(faces)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),-1)
            cv2.addWeighted(img, alpha, output, 1 - alpha, 0, output)
            cv2.rectangle(output,(x,y),(x+w,y+h),(0,255,0),3)

            
        cv2.imshow('video',output)
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()