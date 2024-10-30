"""
File: rocket.py
Name:Jason
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 10


def main():
    """
    make a rocket >> head+belt+upper+lower+belt+head
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    """
    make a rocket head
    """
    for i in range(SIZE):
        #  put " "
        for j in range(SIZE-i):
            print(" ", end="")
        #  put "/"
        for j in range(i+1):
            print("/", end="")
        #  put "\"
        for j in range(i+1):
            print("\\", end="")
        print("")


def belt():
    """
    make a rocket belt,put '+' at the beginning and at the end the middle put '='
    """
    print('+', end='')
    for i in range(SIZE*2):
        print('=', end='')
    print('+')


def upper():
    """
    make a rocket upper,put '|' at the beginning and at the end the middle put '.''/\''.'
    """
    for i in range(SIZE):
        #  put "."
        print('|', end='')
        for j in range(SIZE - i-1):
            print(".", end="")
        #  put "/\"
        for j in range(i + 1):
            print("/", end="")
            print("\\", end="")
        #  put "."
        for j in range(SIZE - i - 1):
            print(".", end="")
        print('|')


def lower():
    """
    make a rocket lower,put '|' at the beginning and at the end the middle put '.''/\''.'
    """
    for i in range(SIZE):
        #  put "."
        print('|', end='')
        for j in range(i):
            print(".", end="")
        #  put "/\"
        for j in range(SIZE-i):
            print("\\", end="")
            print("/", end="")
        #  put "."
        for j in range(i):
            print(".", end="")
        print('|')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
