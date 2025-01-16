'''8. Modify the "Times Table" again so that the user still enters the number of the table,
but if this number is negative the table is printed backwards . So entering"-7" 
would produce the Seven Times Table starting at "12 times" down to "0 times".'''

def table(num):
    if num > 0:
        for i in range(13):
            print(num, "x", i, "=", num * i)
    else:
        num=num*-1
        for i in range(12, -1, -1):
            print(num, "x", i, "=", num * i)

num = int(input("Enter a number: "))
print (f"\nMultiplication Table of {num}\n")
table(num)
