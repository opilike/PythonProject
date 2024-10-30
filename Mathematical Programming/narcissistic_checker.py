"""
File: extension4_narcissistic_checker.py
Name:Jason
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    """
    this program will calculate input check is narcissistic number or not
    then input EXIT number then exit
    """
    print("Welcome to the narcissistic number checker!")
    while True:
        number = int(input("n: "))
        if number == EXIT:
            print("Have a good one!")
            break
        else:
            #  make counter to calculate the number /1 /10 /100 /1000 /10000.....
            counter = 1
            #  make count_number to count the input number of numbers
            count_number = 0
            while True:
                if number // counter == 0:
                    break
                if number < 10:
                    print(str(number) + ' is not a narcissistic number')
                    break
                else:
                    counter = counter*10
                    count_number = count_number+1
            #  take above counter again to calculate the number //1000 //100 //10 %10
            #  it's will more bigger than we want so /10
            counter = int(counter/10)
            #  make total to calculate the number total
            total = 0
            for i in range(count_number):
                #  checked the last numbers yet
                if i == (count_number-1):
                    total = total + ((number % 10) ** count_number)
                else:
                    #  make counter2 for calculate,example 153 we want 5 , then 153//10 ==15   15-10(counter2) = 5
                    #  1654 we want 6 = (1654//100)-((1664//1000)*10) = 6
                    counter2 = int(number // (counter*10))*10
                    total = total + (((number // counter)-counter2) ** count_number)
                counter = int(counter / 10)
            if number == total:
                print(str(number)+' is a narcissistic number')
            else:
                print(str(number) + ' is not a narcissistic number')


if __name__ == '__main__':
    main()
