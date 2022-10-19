#!/usr/bin/env python3
#Exercise 1c
#DESISTO, depois tento melhor.

import cv2
import numpy as np

draw= False
color = (0,0,255)
background=np.ones([400,600,3],dtype=np.uint8)
background.fill(255)


def click_event(event, x, y, flags, params):
    
    global draw      

    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN: 
        draw= True
        
                   
    elif draw  event==cv2.EVENT_MOUSEMOVE:
        cv2.circle(background,(x,y),4,color,-1)
                      
    elif event==cv2.EVENT_LBUTTONUP:
        draw= False
        cv2.circle(background,(x,y),4,color,-1)
        

def main():

    global color

    cv2.namedWindow('Paint.py')
    cv2.setMouseCallback('Paint.py', click_event)

    while True:

        cv2.imshow('Paint.py',background)

        k=cv2.waitKey(1) & 0xFF

        if k == ord('r'):
            color=(0,0,255)
        elif k == ord('g'):
            color=(0,255,0)
        elif k == ord('b'):
            color=(255,0,0)
        elif k==27:
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()