''' Write and test a function that converts a temperature measured in degrees
 centigrade into the equivalent in fahrenheit, and another that does the reverse
 conversion. Test both functions. (Google will find you the formulae)'''

def ctof(tem):
    f=(tem*9/5)+32
    print("Your temperature in fahrenheit is ", f)
def ftoc(tem):
    c=(tem-32)*5/9
    print("Your temperature in celsius is ", c)
temp=int(input("enter the temperature: "))
check=input("did you enter the temperature in celsius or fahrenheit(c/f)?")
if check.lower()=="c":
    ctof(temp)
else:
    ftoc(temp)

