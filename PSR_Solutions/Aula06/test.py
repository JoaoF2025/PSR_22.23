#!/usr/bin/env python3

import cv2

k=cv2.waitKey(1)
while True:
    if k == ord('a'):
        print('Key pressed')
    elif k == ord('q'):
        break
        
    else:
        print('Key Released')

    