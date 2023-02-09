#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Ra-Zakee Muhammad
CSCI051P
2/17/2019
M,W,F 10 am
Assignment 4
This program is a program that creates an electronic painting
of various shapes, flowers, spirals, and polka dots'''

from turtle import *
from random import *

def draw_polygon(n,length):
    '''This function draws a polygon of n sides and of side length 'length'
    param: n, Type int
    param: length, Type int
    return: none, side effect function'''
    for i in range(n):
        angle_turn=360/n
        forward(int(length))
        right(angle_turn)
    #


def draw_spiral(increment,deg,n):
    '''This function draws an incremental spiral
    starting at a provided length and turning
    at a provided degrees and turning n amount of times. These spirals occur at random positions
    param: increment, Type int
    param: deg, Type int
    param: n, Type int
    return: none, side effect function'''
    x = randrange(int((-window_width() / 2) + 100), int((window_width() / 2) - 100), 1)
    #
    y = randrange(int((-window_height() / 2) + 100), int((window_height() / 2) - 100), 1)
    #
    penup()
    #
    setposition(x, y)
    #
    pendown()
    #
    z=1
    #
    while z <= n:
        forward (z*increment)
        right(deg)
        z=z+1
    #



def rotate_repeat(k,n,length, drawing):
    '''This function takes a provided figure and rotates
    and replicates the figure k times
    around the axis of origin for the first figure
    param: k, type int
    param: n, type int
    param: length, type int
    param: drawing, type none, function
    return: none, side effect function'''
    for i in range(k):
        rotate_angle=360/k
        drawing(n,length)
        right(rotate_angle)
    #



def random_circle():
    '''This function generates radius 10 circles inside the window for turtle
    at random positions. If the circles fall of the right they are blue
    and of they fall on the left they are red.
    param: none, type none
    return: none, side effect function'''
    x=randrange(int((-window_width()/2)+20),int((window_width()/2)-20),1)
    #
    y = randrange(int((-window_height() / 2) +20),int((window_height() / 2) - 20) , 1)
    #
    penup()
    #
    setposition(x,y)
    #
    pendown()
    #
    if x>0:
        color='blue'
    #
    else:
        color='red'
    #
    fillcolor(color)
    #
    begin_fill()
    #
    circle(10)
    #
    end_fill()
    #




def drawing_filled_shapes(pos_x,pos_y, fill_color, drawing, sides,side_length):
    '''This function full shapes created in the polygon function
    and fills them with provided colors.
    param: pos_x, Type int
    param: pos_y, Type int
    param: fill_color, Type str
    param: drawing, type none, fucntion
    param: sides: type int
    param: side_length, Type in
    return none, side-effect function'''
    penup()
    #
    setposition(pos_x, pos_y)
    #
    fillcolor(str(fill_color))
    #
    pendown()
    #
    begin_fill()
    #
    drawing(sides, side_length)
    #
    end_fill()
    #




def drawing_colored_spirals(color, increment, degree, n):
    '''This function takes spirals generated
    in the spiral function and draws them using provided pen colors
    param: color, Type str
    param: increment, Type int
    param: deg, Type int
    param: n, Type int
    return: none, side effect function'''
    pencolor(str(color))
    #
    for i in range(2):
        draw_spiral(increment, degree, n)
    #


def monochromatic_flower(pos_x,pos_y,color,k,n,length,drawing):
    '''This function takes repeated figured provided by the
    repetition function and colors them with a provided color.
    param: pos_x, Type int
    param: pos_y, Type int
    param: color, Type str
    param: k, type int
    param: n, type int
    param: length, type int
    param: drawing, type none, function
    return: none, side effect function'''
    penup()
    #
    setposition(pos_x, pos_y)
    #
    fillcolor(str(color))
    #
    pendown()
    #
    begin_fill()
    #
    rotate_repeat(k, n, length, drawing)
    #
    end_fill()
    #


def main():
    '''This main function turns the screen black draws 4 polygons, 5 flowers, 6 spirals, and 20 dots
    param: none, Type none
    return: none, side effect function'''

    bgcolor('black')
    #
    speed(8)
    #
    drawing_filled_shapes(100,-100,'pink',draw_polygon,8,50)
    drawing_filled_shapes(0,0,'orange',draw_polygon,4,75)
    drawing_filled_shapes(-100,100,'purple',draw_polygon,10,50)
    drawing_filled_shapes(-300,250,'green', draw_polygon, 3, 20)
    #
    monochromatic_flower(-200,-50,'green',20,8,50,draw_polygon)
    monochromatic_flower(200, 100, 'orange', 15, 5, 50, draw_polygon)
    monochromatic_flower(-200,100,'pink',7,6,40,draw_polygon)
    monochromatic_flower(200,200,'red',15,7,25,draw_polygon)
    monochromatic_flower(-50,-100,'blue',20,3,50,draw_polygon)
    #
    drawing_colored_spirals('blue',10,90,15)
    drawing_colored_spirals('red',5,45,20)
    drawing_colored_spirals('yellow',1,30,30)
    #
    pencolor('white')
    #
    for i in range(20):
        random_circle()
    #

if __name__ == '__main__':
    main()
    done()
