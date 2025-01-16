'''Functions are often used to validate input. Write afunction that accepts a single
 integer as a parameter and returns Trueif the integer is in the range 0 to 100
 (inclusive), or False otherwise. Write a short program to test the function.'''

def func1(a):
    if a in range(0,100):
        print(True)
    else:
        print(False)
num=int(input("enter any number"))
func1(num)