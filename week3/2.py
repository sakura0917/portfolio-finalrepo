'''Write a program that simulates the way in which a user might choose a password.
The program should prompt for a new password, and then prompt again. If the two
passwords entered are the same the program should say "Password Set" or
similar, otherwise it should report an error.'''
pw1=input("Enter password: ")
pw2=input("Re-enter password: ")
if pw1==pw2:
    print("Password Set!")
else:
    print("The passwords did not match! Please Retry.")