''' Modify the previous program so that it can process any numberof values. The input
 terminates when the user just pressed "Enter" at the prompt rather than entering a
 value.'''
def temp():
    temperatures=[]
    ans="Y"
    x=0
    while ans.upper()=="Y":
        temp=float(input("enter temperature"))
        temperatures.append(temp)
        ans=input("do you want to continue?(Y/N)")
    mx=max(temperatures)
    mn=min(temperatures)
    mean=sum(temperatures)/ len(temperatures)
    print("Maximum Temperature: ",mx)
    print("Minimum temperature:", mn)
    print("Mean of Temperatures: ",mean)
temp()