#!/usr/bin/env python3

#function must have centroid coords as an input
#'s' key for squares, 'e' key for ellipses and 'o' key for circles
#for the cirle, when the 'o' key is pressed the centroid position is the circle origin
#in the ellipse case, 

from traceback import print_list
from typing import final
import cv2
from math import sqrt

def drawCircle(white_board,points,options):

    if points['x'][-1] == -50 :
        points['x'].pop(-1)
        points['y'].pop(-1)

    # If it pops, then it returns and doesnt draw anything, this prevents big lines across to (-50,-50)

    #* ---Checking whether there are enough points to draw a line----
    if len(points['x']) < 2: 
        return
    #It only reaches here if there are enough points to draw a line

    center_point = (points['x'][-2],points['y'][-2] )
    final_point = (points['x'][-1],points['y'][-1] )
    cx,cy=center_point[0], center_point[1]
    rx,ry=final_point[0], final_point[1]
    radius=int(sqrt(((cx-rx)**2)+((cy-ry)**2)))
    #Python passes arguments by assignment, since a np array is mutable, we're just
    #modifying the inicial image, not changing the original memory adress

    cv2.circle(white_board, center_point, radius, options['color'], options['size'])

def drawSquares():
    pass

def drawEllipse():
    pass



