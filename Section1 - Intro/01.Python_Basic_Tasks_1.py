# Write a program that prints in a list the numbers from 0 to 15 (inclusive), 
# each number multiplied by itself, while skipping the numbers 3, 6 and 9.
# Create the list mylist with the numbers from 0 to 15
list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# Create an empty placeholder list to append the solution
mylist = []
# Check if each number in list meets the requirement and raise the ones that DO to the pow of 2
for x in list:
	if x!=3 and x!= 6 and x!= 9:
		x **= 2
		mylist.append(x) 
# Print the new list that satisfies the requirement
print (mylist)