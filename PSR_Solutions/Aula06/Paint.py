#!/usr/bin/env python3
#Exercise 1c

import cv2
from functools import partial
import numpy as np
from colorama import Fore,init

init(autoreset=True)

background=np.ones([400,600,3],dtype=np.uint8)
background.fill(255)

def click_event(event, x, y, flags, params, options):
   
    if event == cv2.EVENT_LBUTTONDOWN: 
        options['draw']= True                  
    elif options['draw'] and event==cv2.EVENT_MOUSEMOVE:
        cv2.circle(background, (x,y), 4, options['color'], -2)                     
    elif event==cv2.EVENT_LBUTTONUP:
        options['draw']=False
        cv2.circle(background,(x,y),4,options['color'],-2)
    
def main():

    options={'draw':False,'color':(0,0,255)}

    cv2.namedWindow('Paint.py')
    cv2.setMouseCallback('Paint.py', partial(click_event, options=options))
    print('You are now drawing in ' + Fore.RED + 'red')

    while True:

        cv2.imshow('Paint.py',background)

        k=cv2.waitKey(1) & 0xFF

        if k == ord('r'):
            options['color']=(0,0,255)
            print('You are now drawing in ' + Fore.RED + 'red')
        elif k == ord('g'):
            options['color']=(0,255,0)
            print('You are now drawing in '+ Fore.GREEN+'green')
        elif k == ord('b'):
            options['color']=(255,0,0)
            print('You are now drawing in '+Fore.BLUE+'blue')
        elif k == ord('c'):
            options['color']=(255,0,0)
            background.fill(255)
            print('Canvas cleared')
        elif k==27:
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()