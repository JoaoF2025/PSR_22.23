#!/usr/bin/env python3
#Exercise 1a, 1b

import cv2

def main():

    image_filename = '/home/joaof2025/PSR_Aulas/psr_22-23/Parte05/images/atlascar.png'
    imagergb = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image


    #cv2.circle(image, center_coordinates, radius, color, thickness)
    h,w,_=imagergb.shape #To get the image dimensions, _ is the color channel, but it won't be used

    center_coords=(w//2,h//2)  #double / so the resut comes as an int
    radius=50
    color=(65,0,255) #comes in rgb
    thickness=2 #comes in pixels
    
    circle_image=cv2.circle(imagergb,center_coords,radius,color,thickness)


    #cv2.putText(image,text,org,font,fontScale,color,thicknes,lineType,bottomLeftOrigin)

    text='PSR'
    font=cv2.FONT_HERSHEY_SIMPLEX
    fontScale=1

    #in order to allign the text some things can be done, like:
    textsize,_=cv2.getTextSize(text,font,fontScale,thickness) #it returns the size of a box containing the text
    org=((w-textsize[0])//2,textsize[1]+100)
    
    text_image=cv2.putText(circle_image,text,org,font,fontScale,color,thickness)
    

    cv2.imshow('Colored Image', imagergb)  # Display the image
    cv2.waitKey(5000) # wait for a key press before proceeding




if __name__ == '__main__':
    main()
