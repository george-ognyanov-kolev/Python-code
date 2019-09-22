# Write a function that prints the type of each element of a list. Test the function by passing the following lists:
#
#    a.	data = [15, 'Python', 15.14, 51+31j, False, ('Python',32), [12, 16, 17]]
#    
#    b.	flatten the [data] list from above, i.e. make sure there is no nesting of elements

data = [15, 'Python', 15.14, 51+31j, False, ('Python',32), [12, 16, 17]]
# Create a new empy list to feed the flattened data into
flatdata = []
# With the for loop and the isinstance function I check if the nested data is list datatype or else
# Append adds items as a single element i.e. the tuple is threated as one item
# Extend adds items threating them as individual elements i.e. the last three numbers from the last list are threated as individual items
# N.B. not sure which solution would be preferable here so left both 
for items in data:
    #if isinstance(items, list):
        #flatdata.extend(items)
    #else:
    flatdata.append(items)
print(flatdata)
def typefunction():
	i=0
	for x in flatdata:
		if i < 100:
			print(type(flatdata[i]))
			i+=1
typefunction()

