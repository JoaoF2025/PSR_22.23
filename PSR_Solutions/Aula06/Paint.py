#!/usr/bin/env python3
#Exercise 1c


import cv2
import numpy as np

leftClick=[]
 

def main(event,x,y):

    global leftClick

    background=np.zeros([400,600,1],dtype=np.uint8)
    background.fill(255)
    print(background.shape)
    cv2.imshow('Background' ,background)


    while True:
        if event==cv2.EVENT_LBUTTONDOWN:
            leftClick=[(x,y)]
            print(leftClick)
        
        k=cv2.waitKey(0)
        if k == 27:
            cv2.destroyAllWindows()
            break



if __name__ == '__main__':
    main()
