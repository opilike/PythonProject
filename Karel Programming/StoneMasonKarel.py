"""
File: StoneMasonKarel.py
Name: Jason
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    Pre-condiction: Karel at left bottom corner
    Post-condiction:Karel finished work and stading at right bottom corner,facing east
    """
    #  karel build a column and then on the top facing east
    while front_is_clear():
        turn_left()
        build_a_column()
        for i in range(3):
            move()
    #  go down and turn left build wall again
        go_down()
    turn_left()
    build_a_column()
    go_down()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


def build_a_column():
    """
    Pre-condition: Karel at left bottom corner,facing east
    Post-condition:Karel build a wall and go to north,facing east or turn around
    """
    #  check first space if no have wall,build it
    if not on_beeper():
        put_beeper()
    while front_is_clear():
        move()
        while not on_beeper():
            put_beeper()
    #  check right is clear or not,if ture turn right,if false turn around   #  try to be good but something weird
    #  it will turn right twice in the top
    # if right_is_clear():
    #     turn_right()
    # else:
    #     turn_around()
    #
    turn_right()


def go_down():
    """
    Pre-condition: Karel at top facing east
    Post-condition:Karel at another column bottom,or just at the bottom,,facing east,
    """
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    #  check front is clear or not,if true move,if false don't move
    if front_is_clear():
        move()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
