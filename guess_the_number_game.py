# Import the "sys" module and the "choice" function from the "random" module
import sys
from random import choice

# Get the first and second command line arguments and convert them to integers
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

# Create a list of numbers from num1 to num2 (inclusive) and choose a random number from that list
numbers = list(range(num1, (num2 + 1)))
ranswer = choice(numbers)

# Loop forever until the user correctly guesses the random number
while True:
    try:
        # Prompt the user to guess a number within the range of num1 and num2
        answer = int(input(f'Guess a number from {num1} and {num2}:'))
        
        # Check if the guessed number is within the range of num1 and num2 and the generated random number is within the range of num1 and num2
        if answer>(num1-1) and ranswer<(num2+1):
            # If the guess is correct, print a message and break out of the loop
            if answer == ranswer:
                print('You are a GENIOUS!!!')
                break
        else:
            # If the guess is outside the range of num1 and num2, print a message
            print('It has to be in between those to numbers!')
    except ValueError:
        # If the user entered something that couldn't be converted to an integer, print a message
        print('Please enter a number')
        continue
