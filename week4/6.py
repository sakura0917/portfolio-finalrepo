''' Write a program that takes a centigrade temperature and displays the equivalent in
 fahrenheit. The input should be a number followed by a letter C. The output should
 be in the same format.'''
temp=input("enter the temperature in celcius (put a 'C' at the end of the value): ")
tem=""
for x in temp:
    if x in "C c":
        a=0
    else:
        tem=tem+x
    a=float(tem)
    f=(a*9/5)+32
print("Your temperature in fahrenheit is ", f," F")           