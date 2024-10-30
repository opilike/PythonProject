"""
File: MidpointKarel.py
Name: Jason
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel at left bottom corner
    Post-condition:Karel finished work and stading at middle of first row , and put peeper
    """
    find_the_destination()
    if not on_beeper():
        put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


def find_the_destination():
    """
    Pre-condition: Karel at left bottom corner
    Post-condition:Karel finished work and standing at middle of bottom row
    """
    #  move 1 step to the east and turn to north move 2 steps
    #  check if east clear or if facing north turn to east(initially facing east)
    while front_is_clear():
        if facing_north():
            turn_right()
        move()
        turn_left()
        #  check front is clear if not break!
        if front_is_clear():
            move()
            if front_is_clear():
                move()
    #  on the top middle and then turn back
    turn_around()
    #  walk to the middle of bottom row
    while front_is_clear():
        move()
    #  make Karel facing east !
    if facing_south():
        turn_left()
    else:
        if facing_west():
            turn_around()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
