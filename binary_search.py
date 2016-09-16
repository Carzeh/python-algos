import sys
import math
from yes_or_no import query_yes_no

min = 1
max = 1

def binary_search(maxNumber):
    max = int(maxNumber)
    global min

    guess = ((max - min) / 2) + min
    guess = int(guess)

    # Guess half way between 1 and max number
    answer = query_yes_no('Is your number ' + str(guess) + '?')

	# Return guess and ask if correct
    if answer is True:
    	print('Your number is ' + str(guess))
    else:
    	# If not correct then ask if higher or lower
    	higherNumber = query_yes_no('Is your number higher?')

    	# If higher set min to guess + 1
    	if higherNumber is True:
    		min = guess + 1
    	# If lower set max to maxNumber - 1
    	else:
    		max = guess - 1
    	binary_search(max)

    return 'error'

maxNumber = raw_input('What is your max number? ')
binary_search(maxNumber)
