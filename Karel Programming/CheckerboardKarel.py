"""
File: CheckerboardKarel.py
Name: Jason
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.

Karel's destination is right top corner,facing east
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel at left bottom corner
    Post-condition:Karel finished work and stading at right top corner,facing east
    """
    #  put first peeper
    put_beeper()
    #  check front is clear or not
    while front_is_clear():
        fill_one_line()
    #  check if north have space can walk,if can walk !
    if facing_east():
        if left_is_clear():
            turn_left()
            if front_is_clear():
                fill_one_line()
    #  check if Karel stop in destination , just practice !
    check_in_destination()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


def fill_one_line():
    """
    Pre-condition: Karel at left bottom corner
    Post-condition:Karel put 1 peeper leave one space blank amd put 1 peeper finished and go top row,and put peeper
    """
    #  check front is clear
    while front_is_clear():
        move()
        #  check second front is clear and put beeper
        if front_is_clear():
            move()
            put_beeper()
    #  check if facing east or not, if true turn to left, if false turn to right,make Karel facing north
    if facing_east():
        #  Karel facing north
        turn_left()
        #  check last space have beeper or not,and check have another row can go or not
        if not on_beeper():
            if front_is_clear():
                move()
                turn_left()
                put_beeper()
        else:
            if front_is_clear():
                move()
                turn_left()
                move()
                put_beeper()
    #  Karel facing west
    else:
        #  Karel facing north
        turn_right()
        #  check last space have beeper or not,and check have another row can go or not
        if not on_beeper():
            if front_is_clear():
                move()
                turn_right()
                put_beeper()
        else:
            if front_is_clear():
                move()
                turn_right()
                move()
                put_beeper()


def check_in_destination():
    """
    Pre-condition: Karel just finished work !
    Post-condition:Karel at right top corner,facing east
    """
    # check if Karl facing_est or not
    if not facing_east():
        if facing_north():
            turn_right()
            while front_is_clear():
                move()
    else:
        while front_is_clear():
            move()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
