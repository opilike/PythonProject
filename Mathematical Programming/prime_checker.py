"""
File: prime_checker.py
Name:Jason
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT = -100
# import time


def main():
	"""
	this program check the input is prime number or not
	then input EXIT number then exit
	"""

	#  Print text first
	print('Welcome to the prime checker!')
	while True:
		number = int(input('n: '))
		#  Check number is EXIT or not
		if number == EXIT:
			print("Have a good one!")
			break
		#  Check number is 2 or not
		elif number == 2:
			print(str(number) + " is a prime number.")
		else:
			#  give a number_count to count the remainder of something less than itself
			#  give check,if check == 1 it's prime number,elif check == 0 it's not prime number
			# number_count = 2
			check = 1
			# start = time.time()
			#  give a number_count to count the remainder of something less than itself,number-1
			#  because from 2, so number-2
			# for i in range(number-2):
			# 	if number % number_count == 0:
			# 		check = 0
			# 		#  if find it then break
			# 		break
			# 	number_count = number_count + 1
			for i in range(2, int(number ** 0.5) + 1, 1):
				if number % i == 0:
					check = 0
					break
			# end = time.time()
			# print("執行時間：%f 秒" % (end - start))
			if check == 0:
				print(str(number) + " is not a prime number.")
			elif check == 1:
				print(str(number) + " is a prime number.")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
