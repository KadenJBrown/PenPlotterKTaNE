from madison_axi.axi import *
import random

initialize()

def space_x():
    pen_up()
    point_in_direction(0)
    move_forward(15)

def space_y():
    pen_up()
    point_in_direction(90)
    move_forward(-15)

def draw_border():
    pen_down()
    point_in_direction(0)
    for _ in range(4):
        turn_left(90)
        move_forward(150)

move_to(-250,180)
point_in_direction(0)
"""move_forward(500)
point_in_direction(270)
move_forward(360)
point_in_direction(180)
move_forward(500)
point_in_direction(90)
move_forward(360)"""
#space_x()
#space_y()
draw_border()
cleanup()
