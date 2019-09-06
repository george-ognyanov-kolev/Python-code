#Write a function that prints the type of each element of a list. Test the function by passing the following lists:
#
#    a.	data = [15, 'Python', 15.14, 51+31j, False, ('Python',32), [12, 16, 17]]
#    
#    b.	flatten the [data] list from above, i.e. make sure there is no nesting of elements

data = [15, 'Python', 15.14, 51+31j, False, ('Python',32), [12, 16, 17]]
flatdata = []
for items in data:
    if isinstance(items, list):
        flatdata.extend(items)
    else:
        flatdata.append(items)
print(flatdata)
def typefunction():
	i=0
	for x in flatdata:
		if i < 100:
			print(type(flatdata[i]))
			i+=1
typefunction()