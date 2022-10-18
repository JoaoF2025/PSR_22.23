#!/usr/bin/env python3
#Exercise 2d e 2e

import cv2
import numpy

def main():

    image_filename = '/home/joaof2025/PSR_Aulas/psr_22-23/Parte05/images/atlas2000_e_atlasmv.png'
    imagergb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    
    lower_bound_rgb=numpy.array([0,90,0])
    upper_bound_rgb=numpy.array([50,255,50])
    imageg=cv2.inRange(imagergb,lower_bound_rgb,upper_bound_rgb)

    #
    lower_bound_hsv=numpy.array([50,100,100])
    upper_bound_hsv=numpy.array([70,255,255])
    image_hsv = cv2.cvtColor(imagergb, cv2.COLOR_BGR2HSV)
    image_hsv_g=cv2.inRange(imagergb, lower_bound_hsv,upper_bound_hsv)

    cv2.imshow('RGB Image',imagergb )
    #cv2.imshow('Only Green Image', imageg)s
    cv2.imshow('Only Green Image but with HSV now', image_hsv)
    cv2.waitKey(5000) # wait for a key press before proceeding



if __name__ == '__main__':
    main()
