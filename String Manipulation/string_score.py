"""
File: string_score.py
Name:Jason
------------------------------
This program calculates a score for a given string based on 
the types of characters it contains. It assigns points as follows: 
digits are worth 1 point, uppercase letters are worth 2 points, 
and lowercase letters are worth 3 points. The score() function 
goes through each character in the string, adds up the points 
according to its type, and then prints out the total score.
"""


def main():
    """
    make a function if string like digit->+1 ; upper->+2; lower->+3
    """
    score('1aB4rC')    # digit->1 ; upper->2; lower->3
    # 12
    score('aaaaA3')
    # 15


def score(string):
    #  give a number to count !
    number = 0
    for i in range(len(string)):
        #  check if lower
        if string[i].islower():
            number += 3
        #  check if upper
        elif string[i].isupper():
            number += 2
        #  check if digit
        else:
            number += 1
    return print(str(number))


if __name__ == '__main__':
    main()