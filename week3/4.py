'''Modify your program again so that the chosen password cannot be one of a list of
 common passwords, defined thus:
 BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']'''
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
print("The password should be atleast 8 character long")
print("(not longer than 12 character)")
pw1=input("Enter password: ")
pw2=input("Re-enter password: ")
if pw1 in BAD_PASSWORDS:
    print("Password too common.")
    print("Please choose a stronger password!")
else:
 if pw1==pw2:
    if len(pw1)>=8 and len(pw1)<=12:
        print("Password Set!")
    else:
        print("the password length must be between 8 and 12")
 else:
    print("The passwords did not match! Please Retry.")
