"""
File: weather_master.py
Name:Jason
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100


def main():
	"""
	This program is help to calculate,the average,
	highest, lowest, cold days among the user's input,then input EXIT number then exit
	"""
	#  Print text first
	print("stanCode \"Weather Master 4.0\"!")
	data = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
	#  initialization
	#  counter for count how many data
	#  count_day for count how many cold day
	#  Average_number for count average temperatures
	count_number = 0
	count_day = 0
	average_number = 0
	#  data_ total
	total_data = 0
	if data == EXIT:
		print('No temperatures were entered.')
	else:
		#  initialize the data
		maximum = data
		minimum = data
		while True:
			#  if data = Exit then exit program
			if data == EXIT:
				break
			#  check data bigger than 16 or not !
			if data < 16:
				count_day = count_day+1
			#  when data input count_number+1
			count_number = count_number+1
			#  when data input total+data
			total_data = total_data + data
			if count_number == 0:
				count_number = 1
			#  if data < minimum reassign the maximum
			if data > maximum:
				maximum = data
			#  if data < minimum reassign the minimum
			if data < minimum:
				minimum = data
			average_number = float(total_data / count_number)
			data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(average_number))
		print(str(count_day) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
