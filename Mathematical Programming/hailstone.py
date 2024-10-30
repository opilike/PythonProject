"""
File: hailstone.py
Name: Jason
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    the input will calculate the input use the execution of the Hailstone sequence,and give how many steps!
    """
    #  Print text first
    print("This program computes Hailstone sequences.\n")
    #  number is input data
    #  count is count how many steps
    number = int(input('Enter a number: '))
    count = 0
    if number == 1:
        print('It took '+str(count)+' steps to reach 1.')
    else:
        while True:
            if number != 1:
                count = count+1
                #  check is even number or odd number
                if number % 2 == 0:
                    print(str(number)+' is even, so I take half: '+str((number // 2)))
                    number = number // 2
                else:
                    print(str(number) + ' is odd, so I make 3n+1: ' + str((number*3+1)))
                    number = int(number * 3 + 1)
            if number == 1:
                break
        print('It took '+str(count)+' steps to reach 1.')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
