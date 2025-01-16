''' 7. Modify your "Times Table" program so that the user enters the number of the table
they require. This number should be between 0 and 12 inclusive.'''

def table(num):
    print (f"\nMultiplication Table of {num}\n")
    for i in range(13):
        result = i*num
        print(f"{i} x {num} = {result}")
num=int(input("enter a number between 0 and 12"))
table(num)