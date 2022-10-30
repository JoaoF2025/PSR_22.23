#!/usr/bin/env python3

import cv2
import numpy as np

def keyboardEvents(switcher):
    k=cv2.waitKey(1) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
        exit()
    elif k == ord('v'):
        switcher['counter'] = not switcher['counter']
        print(switcher)


def switchOutput(background, image_flip,switcher):
   
    mask = cv2.inRange(background,(0,0,0),(0,0,255))
    mask = mask.astype(bool)

    if switcher['counter']:
        image_flip[mask] = background[mask]  #! joins the circle and the camera image

    
def main():
    # initial setup
    cam = cv2.VideoCapture(0)

    background=np.zeros((480,640,3),dtype=np.uint8)
    background.fill(255)

    switcher={'counter':False}

    while True:

        _, image = cam.read()  # get an image from the camera
        image_flip=cv2.flip(image,1)
        
        cv2.circle(background,(int(image.shape[0]/2),int(image.shape[1]/2)),90,(0,0,255),-2)

        keyboardEvents(switcher)
        switchOutput(background,image_flip,switcher)

        cv2.imshow('Imagem', image_flip)

if __name__ == '__main__':
    main()