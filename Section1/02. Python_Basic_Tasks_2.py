# Write a program that prints the Fibonacci Sequence 
# (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, ...)
# from the 5th till the 15th element of the sequence.
# Define two variables respectively for the 0 and 1 POSITION of the sequence in list
# It so happens those two variable are the actual numbers in sequence as well
a = 0
b = 1
list1 = [a, b]
# The variable x is how the sequence works - the last two numbers summed up to form the new number
# Itterate this bitch a couple of times to generate the sequence and grab the list from the 5 till 15 number IN SEQUENCE, NOT IN LIST
while a<16 and b<17:
	x = list1[a] + list1[b]
	a+=1
	b+=1
	list1.append(x)
print(list1[4:16])