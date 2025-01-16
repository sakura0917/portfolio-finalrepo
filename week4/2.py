'''Write a function that has a single string as its parameter, and returns the number of
 uppercase letters, and the number of lowercase letters in the string. Test the
 function with a short program.'''

def uplow(name):
    up=0
    low=0
    for x in name:
        if x==x.upper():
            up+=1
        else:
            low+=1
    print("upper case letters=", up)
    print("lower case letters=", low)

uplow("sAKURA")