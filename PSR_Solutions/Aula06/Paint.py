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

    while True:
        c= cv2.waitKey(20)
        if c==114:
            color=(0,0,255)
        if c==98:
            color(255,0,0)
        if c==103:
            color=(0,255,0)    

    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN: 
        draw= True

            
    elif event==cv2.EVENT_MOUSEMOVE:
        if draw==True:
            cv2.circle(background,(x,y),7,color,-1)
           
        

    elif event==cv2.EVENT_LBUTTONUP:
        draw= False
        cv2.circle(background,(x,y),7,color,-1)
        

def main():

    cv2.namedWindow('Paint.py')
    # setting mouse handler for the image and calling the click_event() function
    cv2.setMouseCallback('Paint.py', click_event)

# close the window when ESC is pressed
    while True:
        cv2.imshow('Paint.py',background)
        k=cv2.waitKey(20) & 0xFF
        if k==27:
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()