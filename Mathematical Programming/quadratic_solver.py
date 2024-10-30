"""
File: quadratic_solver.py
Name: Jason
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	""""
	This program to compute the roots of equation ax^2 + bx + c = 0, find the result
	"""
	#  Print text first
	print("StanCode Quadratic Solver!")
	#  tell user give A
	input_a = int(input('Enter a: '))
	#  if a = 0 , break !
	if input_a == 0:
		print('Please give number > 0 !')
	else:
		input_b = int(input('Enter b: '))
		input_c = int(input('Enter c: '))
		#  give discriminant
		discriminant = int(input_b**2 - 4*input_a*input_c)
		#  if discriminant<0 print No real roots,reduce calculate
		if discriminant < 0:
			print('No real roots', end="")
		#  if discriminant=0 print One roots ,reduce calculate
		elif discriminant == 0:
			output_x = float((-input_b/2*input_a))
			print("One root: " + str(output_x), end="")
		else:
			#  if discriminant>0 print two roots ,do two time and print!
			output_x = float(((-input_b + math.sqrt(discriminant)) / (2 * input_a)))
			output_x2 = float(((-input_b - math.sqrt(discriminant)) / (2 * input_a)))
			print("Two roots: " + str(output_x) + ", " + str(output_x2), end="")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
