"""
File: coin_flip_runs.py
Name:Jason
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""
import random


def main():
	"""
	user give a num_run and random flip,print the result according to num_run
	"""
	print('Let\'s flip a coin!')
	num_run = int(input('Number of runs: '))
	#  make st be output string
	st = ''
	can_add = True
	run = 0
	#  make tt2 a single string(first one)
	tt = flip(random.randint(0, 2))
	st += tt
	while True:
		if run == num_run:
			break
		else:
			#  make tt2 a single string(second one)
			tt2 = flip(random.randint(0, 2))
			st += tt2
			#  if match run+1 and if next one different make 'can_add' be true them make false
			if tt == tt2:
				if can_add:
					run += 1
					can_add = False
			else:
				can_add = True
			tt = tt2
	print(str(st))


def flip(num):
	if num == 0:
		return 'H'
	else:
		return 'T'


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
