# Write a function that prompts the user for a string and then prints out weather the string is read the same forwards and backwards, e.g. “Level”
def myfunc():
    var = input("Enter string: ")
    rav = var[::-1]
    a = var.replace(' ','')
    b = rav.replace(' ','')
    if a == b:
        return True
    else:
        return False
myfunc()