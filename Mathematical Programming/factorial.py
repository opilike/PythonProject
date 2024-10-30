"""
File: extension1_factorial.py
Name: Jason
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
	"""
	This calculate the factorial result of the number,then input EXIT number then exit
	"""
	#  Print text first
	print("Welcome to stanCode factorial master!")
	while True:
		number = int(input("Give me number, and I will list the answer of factorial: "))
		#  if user type EXIT number then leave
		if number == EXIT:
			print("- - - - - -  See ya! -------------")
			break
		else:
			#  counter for counter number 1 2 3 4 5 6
			counter = 1
			#  final_number for result number
			final_number = 1
			#  1*1 1*2 2*3 6*4 ..........
			for i in range(number-1):
				counter = counter + 1
				final_number = final_number*counter
			print('Answer: '+str(final_number))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
