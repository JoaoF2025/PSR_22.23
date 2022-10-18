#!/usr/bin/env python3
#Exercise 2f
#ACABAR

from email.mime import image
import cv2
import numpy

def main():

    image_filename = '/home/joaof2025/PSR_Aulas/psr_22-23/Parte05/images/atlas2000_e_atlasmv.png'
    imagergb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    cv2.imshow('Imagem Original',imagergb)
    
    lower_bound_rgb=numpy.array([0,80,0])
    upper_bound_rgb=numpy.array([40,255,50])
    image_mask=cv2.inRange(imagergb,lower_bound_rgb,upper_bound_rgb)
    cv2.imshow('Only Green Part',image_mask)

    image_mask=image_mask.astype.bool

    imgb,imgg,imgr=cv2.split()
    
    imgb*[image_mask]=0
    imgg*[image_mask]=0
    imgr*[image_mask]=255


    cv2.waitKey(5000) # wait for a key press before proceeding



if __name__ == '__main__':
    main()
