"""
File: CollectNewspaperKarel.py
Name: Jason
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condition: Karel at top left corner
    Post-condition:Karel pick up the newspaper and then return to its initial position
    """
    go_pick_newspaper()
    go_back()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


def go_pick_newspaper():
    """
    Pre-condition: Karel at top left corner
    Post-condition:Karel go to the destination pick up the newspaper
    """
    #  move to the right corner
    while front_is_clear():
        move()
    turn_right()
    #  move to the destination
    move()
    turn_left()
    move()
    #  at the destination pick up the newspaper
    if on_beeper():
        pick_beeper()


def go_back():
    """
    Pre-condition:  Karel at the destination pick up the newspaper
    Post-condition: Karel go back and put the newspaper
    """
    turn_around()
    #  move to the left
    while front_is_clear():
        move()
    turn_right()
    # move to the top left corner
    while front_is_clear():
        move()
    #  turn to the initial position
    turn_right()
    #  put_newspaper
    put_beeper()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
