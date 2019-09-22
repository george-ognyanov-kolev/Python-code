# Write a function which generates unique passwords. 
# The passwords should contain - lowercase letters, uppercase letters, numbers, and the following symbols: !@#$%^&*()?

# https://www.geeksforgeeks.org/generating-random-ids-python/
# https://docs.python.org/2/library/string.html

# Import the two libraries needed to randomize shit and work with strings
import random
import string
# Define a variable for the user to choose how long the password will be
# Convert said variable to integer because range wouldn't take string values
def passfunc():
	var = int(input("Enter string: "))
	password = '' . join([random.choice(string.hexdigits + "!@#$%^&*()?") 
		for n in range(var)])
	print (password)
passfun()