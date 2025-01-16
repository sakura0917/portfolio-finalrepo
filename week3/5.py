''' Modify your program a final time so that it executes until the user successfully
 chooses a password. That is, if the password chosen fails any of the checks, the
 program should return to asking for the password the first time.'''
'''Modify your program again so that the chosen password cannot be one of a list of
 common passwords, defined thus:
 BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']'''
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

print("The password should be at least 8 characters long (but not longer than 12 characters).")

answer = True
while answer:
    pw1 = input("Enter password: ")
    pw2 = input("Re-enter password: ")

    if pw1 in BAD_PASSWORDS:
        print("Password too common. Please choose a stronger password!")
    elif pw1 != pw2:
        print("The passwords did not match! Please try again.")
    elif len(pw1) < 8 or len(pw1) > 12:
        print("The password length must be between 8 and 12 characters. Please try again.")
    else:
        print("Password Set!")
        answer = False

