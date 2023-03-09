import sys
from random import choice

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

numbers = list(range(num1, (num2 + 1)))
ranswer = choice(numbers)


while True:
	try:
		answer = int(input(f'Guess a number from {num1} and {num2}:'))
		if answer>(num1-1) and ranswer<(num2+1):
			if answer == ranswer:
				print('You are a GENIOUS!!!')
				break
		else:
			print('It has to be in between those to numbers!')
	except ValueError:
		print('Please enter a number')
		continue