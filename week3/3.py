'''Modify your previous program so that the password must be between 8 and 12
characters (inclusive) long.'''
print("The password should be atleast 8 character long")
print("(not longer than 12 character)")
pw1=input("Enter password: ")
pw2=input("Re-enter password: ")
if pw1==pw2:
    if len(pw1)>=8 and len(pw1)<=12:
        print("Password Set!")
    else:
        print("the password length must be between 8 and 12")
else:
    print("The passwords did not match! Please Retry.")
