"""
File: extension2_number_checker.py
Name: Jason
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    this program check what type of input number give a result! ,then input EXIT number then exit
    """
    #  Print text first
    print('Welcome to the number checker!')
    while True:
        number = int(input('n: '))
        #  Check number is EXIT or not
        if number == EXIT:
            print("Have a good one!")
            break
        else:
            #  give a number_count to count the remainder of something less than itself
            number_count = 1
            #  give a total to calculate all factor sum !
            total = 0
            #  give a number_count to count the remainder of something less than itself,number-1
            for i in range(number - 1):
                #  find all factor
                if number % number_count == 0:
                    total = total+number_count
                number_count = number_count + 1
            if total > number:
                print(str(number)+" is an abundant number")
            elif total == number:
                print(str(number) + " is a perfect number")
            else:
                print(str(number) + " is a deficient number")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
