#!/usr/bin/env python3

import cv2
import numpy as np
from pynput import keyboard
from math import sqrt
from functools import partial

def mousePosition(event, x, y, flags, params, options, background):
    if event == cv2.EVENT_MOUSEMOVE:         
        options['x'],options['y']=x,y  
        cv2.circle(background, (x,y), 3, options['color'], -1)

"""""
def keyListener():
    
    def on_press(key):
        if 'char' in dir(key) and key.char == 'p':
            print('p pressed')
        elif 'char' in dir(key) and key.char == 'o':
            print('o pressed')
        elif 'char' in dir(key) and key.char == 'e':
            print('e pressed')

    def on_release(key):
        if 'char' in dir(key) and key.char == 'p':
            print('p released')
        elif 'char' in dir(key) and key.char == 'o':
            print('o released')
        elif 'char' in dir(key) and key.char == 'e':
            print('e released')

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
"""""


def drawCircle(options,background):
    circle_flip = options['circle_flip']

    if circle_flip == 1:
        options['ix'], options['iy'] = options['x'], options['y']
        options['circle_flip'] = 2    
    elif circle_flip == 3:
        options['x1'], options['y1'] = options['x'], options['y']
        background_copy = background.copy()
        cv2.rectangle(background_copy, (options['ix'], options['iy']), (options['x1'], options['y1']), options['color'])
        cv2.imshow('Canvas', background_copy)
        circle_flip = 0

def main():         

    options={'color':(0,0,255), 'x':-1, 'y':-1, 'ix': -1, 'iy': -1, 'x1': -1, 'y1': -1, 'circle_flip': 0}

    background=np.ones([400,600,3],dtype=np.uint8)
    background.fill(255)

    while(1):

        cv2.namedWindow('Canvas')
        cv2.setMouseCallback('Canvas', partial(mousePosition, options=options, background=background))

        drawCircle(options,background)    
        cv2.imshow('Canvas', background)
        

        k=cv2.waitKey(1) & 0xFF

        if k == 27:
            cv2.destroyAllWindows
            break
        elif k == ord('a'):
            options['circle_flip'] += 1

if __name__ == '__main__':
    main()