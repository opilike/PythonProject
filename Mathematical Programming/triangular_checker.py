"""
File: extension3_triangular_checker.py
Name:Jason
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""
import math
EXIT = -100


def main():
    """
    this program will calculate input check is triangular number or not
    then input EXIT number then exit
    """
    print("Welcome to the triangular number checker!")
    while True:
        number = int(input("n: "))
        if number == EXIT:
            print("Have a good one!")
            break
        #  make formula to be n*n+n-2*number = 0
        #  use quadratic_solver to find result,if the result is int then it's triangular number !
        else:
            #  use counter to calculate b^2-4ac
            counter = int(1+8*number)
            #  if the formula remainder after dividing by 2 == 0,it triangular number!
            if (-1+math.sqrt(counter)) % 2 == 0:
                print(str(number)+" is a triangular number")
            else:
                print(str(number) + " is not a triangular number")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
