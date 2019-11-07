from madison_axi.axi import *
from random import *

initialize()

size = 150
width = 30
height = 70
timer_pos = randrange(2)

def space_x(forward):
    pen_up()
    point_in_direction(0)
    move_forward(forward)

def space_y(forward):
    pen_up()
    point_in_direction(90)
    move_forward(forward)

def draw_border():
    point_in_direction(0)
    pen_down()
    point_in_direction(0)
    for _ in range(4):
        turn_left(90)
        move_forward(size)
    pen_up()

def draw_character(what):
    point_in_direction(0)
    if what == ":":
        pen_up()
        move_to((width/2)+get_x(),get_y()+(height/4))
        pen_down()
        pen_up()
        move_to(get_x(),get_y()+(height/2))
        pen_down()
        pen_up()
        move_to(get_x()-(width/2),get_y()-(height*(3/4)))
    if what == 1:
        pen_up()
        turn_left(90)
        move_forward(height)
        turn_right(90)
        pen_down()
        move_forward(width/2)
        turn_right(90)
        move_forward(height)
        turn_left(90)
        move_forward(width/2)
        move_forward(width*-1)
    if what == 2:
        pen_down()
        move_forward(width)
        move_forward(-1*width)
        turn_left(90)
        move_forward(height/2)
        turn_right(90)
        move_forward(width)
        turn_left(90)
        move_forward(height/2)
        turn_left(90)
        move_forward(width)
        pen_up()
        move_to(get_x(),get_y()-height)
    if what == 3:
        pen_down()
        move_forward(width)
        for _ in range(2):
            move_to(get_x(),get_y()+(height/2))
            move_forward(-1*width)
            move_forward(width)
        pen_up()
        move_to(get_x()-width,get_y()-height)
    space_x(10)

def draw_timer():
    space_x(20)
    original_pos = get_position()
    draw_character(randrange(1,4))
    space_x((width+3)//2)
    draw_character(":")
    space_x(width//2)
    for _ in range(2):
        draw_character(randrange(1,4))
        space_x(width+3)
    pen_up()
    move_to(original_pos[0],original_pos[1])

def draw_mod(modchoice):
    space_x(20)
    # 0=Button 1=Circle 2=Keypad
    if modchoice == 0:
        sides = randrange(3,7)
        pen_down()
        for _ in range(sides):
            move_forward(size//sides)
            turn_left(360//sides)
    if modchoice == 2:
        sides = range(4)
        pen_down()
        for _ in range(3):
            for _ in range(sides):
                move_forward(size//sides)
                turn_left(360//sides)
            move_forward(size//sides)

# Draw module borders
move_to(-350,220)
point_in_direction(0)
for _ in range(2):
    space_y(-15-size)
    for _ in range(3):
        space_x(15+size)
        draw_border()
    move_to(-350,get_y())
# Start filling in modules
move_to(-350,220)
# Timer or module (Mod 0)
space_y(-15-(3*(size//4)))
if timer_pos == 0:
    draw_timer()
else:
    draw_mod(2)
space_x(size)
# Other one (Mod 1)
if timer_pos == 1:
    draw_timer()
else:
    draw_mod(2)
cleanup()
