''' 1. Write a function that accepts a positive integer as a parameter and then returns
 a representation of that number in binary (base 2).
 Hint: This is in many ways a trick question. Think!'''

def convertBinary(a):
    if a > 0:
        return bin(a)[2:]
    else:
        return "Please enter a positive number!"

num=int(input("enter a positive number"))
binForm = convertBinary(num)
print(f"The binary representation of {num} is {binForm}.")
