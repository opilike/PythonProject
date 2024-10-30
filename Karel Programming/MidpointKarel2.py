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
    Post-condition:Karel finished work at middle of first row,put 1 peeper facing east
    """
    find_the_destination2()
    clear_beeper()
    # if facing west make Karel facing east
    if facing_west():
        turn_around()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


def find_the_destination2():
    """
    Pre-condition: Karel at left bottom corner
    Post-condition:Karel put every 1 peeper in every row and  middle of first row,put 2 peeper
    """
    #  put peeper at first and end
    while not on_beeper():
        put_beeper()
    while front_is_clear():
        move()
    put_beeper()
    turn_around()
    if front_is_clear():
        move()
    #  check if not on peeper，if not on beeper move
    while not on_beeper():
        #  check next step is clear
        while front_is_clear():
            move()
        turn_around()
        # check if on beeper or not, if on beeper move and put 1 beeper
        while on_beeper():
            if front_is_clear():
                move()
        put_beeper()
        #  check next step have beeper or not,move back
        #  that's middle place is behind Karel and put 1 beeoer
        if front_is_clear():
            move()
        if on_beeper():
            turn_around()
            if front_is_clear():
                move()
    # check for 1x1 map & 2x2 map
    if facing_west():
        turn_around()
        if front_is_clear():
            put_beeper()
    if front_is_clear():
        put_beeper()


def clear_beeper():
    """
    Pre-condition:Karel put every 1 peeper in every row and  middle of first row,put 2 peeper
    Post-condition:Karel finished work at middle of first row,put 1 peeper facing east
    """
    #  check for 1x1 map, if not clear all map, if do just clear 1
    #  pick up and move till the wall
    if front_is_clear():
        while front_is_clear():
            move()
            if on_beeper():
                pick_beeper()
        #  turn around
        turn_around()
        #  pick up peeper at at the corner
        if on_beeper():
            pick_beeper()
        #  return to the other side
        while front_is_clear():
            move()
        turn_around()
        #  if have peeper pick up and move
        while on_beeper():
            pick_beeper()
            if front_is_clear():
                move()
        #  return back the middle place !
        turn_around()
        if front_is_clear():
            move()
    #  for 1x1 map just pick up 1 beeper
    else:
        pick_beeper()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
