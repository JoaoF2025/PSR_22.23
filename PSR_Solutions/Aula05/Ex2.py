#!/usr/bin/env python3
#Exercise 2a, 2b and 2c
#Review 2c
import cv2

def main():

    image_filename = '/home/joaof2025/PSR_Aulas/psr_22-23/Parte05/images/atlascar2.png'
    imagergb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    imggray=cv2.cvtColor(imagergb, cv2.COLOR_BGR2GRAY)
    retval, image_thresholded = cv2.threshold(imggray, 128, 255, cv2.THRESH_BINARY)
    image_thresholded2 = imagergb >128

    b,g,r=cv2.split(imagergb)
    image_thresholdedb = cv2.threshold(b, 50, 255, cv2.THRESH_BINARY)
    image_thresholdedg = cv2.threshold(g, 100, 255, cv2.THRESH_BINARY)
    image_thresholdedr = cv2.threshold(r, 150, 255, cv2.THRESH_BINARY)
    mergedimage=cv2.merge((b,g,r))


    print(imagergb.shape)
    print(imggray.shape)

    print(image_thresholded.dtype)
    print(image_thresholded2.dtype)

    print(mergedimage.dtype)


    #cv2.imshow('Colored Image', imagergb)  # Display the image
    #cv2.imshow('Gray Image', imggray) 
    #cv2.imshow('Image Treshhold', image_thresholded)
    cv2.imshow('Merged Image', mergedimage)
    cv2.waitKey(5000) # wait for a key press before proceeding




if __name__ == '__main__':
    main()
