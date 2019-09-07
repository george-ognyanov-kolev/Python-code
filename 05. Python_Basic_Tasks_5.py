# Write a function that prompts the user for an input integer and then prints out all of the divisors of this number.
def myfunc():
    x = int(input("Enter and integer number: "))
    i = 1
    while i<x:
        if x % i == 0:
            print(i)
        i=i+1
myfunc()