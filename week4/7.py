''' Write a program that reads 6 temperatures (in the same format as before), and
 displays the maximum, minimum, and mean of the values.
 Hint: You should know there are built-in functions for max and min. If you hunt, you
 might also find one for the mean.'''
def temp():
    print("enter 6 temperatures")
    temperatures=[]
    for x in range(6):
        temp=float(input(f"temperature{x+1}: "))
        temperatures.append(temp)
    mx=max(temperatures)
    mn=min(temperatures)
    mean=sum(temperatures)/ len(temperatures)
    print("Maximum Temperature: ",mx)
    print("Minimum temperature:", mn)
    print("Mean of Temperatures: ",mean)
temp()