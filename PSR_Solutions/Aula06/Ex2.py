#!/usr/bin/env python3
#Exercise 2a and 2b

import cv2

def main():
    # initial setup
    cam = cv2.VideoCapture(0)
    window_name = 'A5-Ex2'
    cv2.namedWindow(window_name,cv2.WINDOW_AUTOSIZE)

    while True:
        _, image = cam.read()  # get an image from the camera
        image_flip=cv2.flip(image,1)
        cv2.imshow(window_name,image_flip)
        if cv2.waitKey(20) == 27:
            cv2.destroyAllWindows()
            break
    
    cam.release()

if __name__ == '__main__':
    main()
