#!/usr/bin/env python3
#Exercise 1
#ACABAR DE BRINCAR

import cv2
import argparse



def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', required=False,help='Full path to image file.', default='/home/joaof2025/PSR_Aulas/psr_22-23/Parte05/images/atlascar.png')
    args = parser.parse_args()


    path1=args.image
    path2='/home/joaof2025/PSR_Aulas/psr_22-23/Parte05/images/atlascar.png' if path1=='/home/joaof2025/PSR_Aulas/psr_22-23/Parte05/images/atlascar2.png' else '/home/joaof2025/PSR_Aulas/psr_22-23/Parte05/images/atlascar2.png'
    img1=cv2.imread(path1,cv2.IMREAD_COLOR)
    img2=cv2.imread(path2, cv2.IMREAD_COLOR)



    while True:
        
        numrand=1
        
        if (numrand/2==0):
            cv2.imshow('Imagem 1',img1)
            numrand =+1
            cv2.waitKey(3000)
        else:
            cv2.imshow('Imagem 2',img2)
            numrand =+1
            cv2.waitKey(3000)




if __name__ == '__main__':
    main()
