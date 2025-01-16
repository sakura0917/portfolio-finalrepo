'''3. Write a program that takes a bunch of command-line arguments, and then prints
out the shortest. If there is more than one of the shortest length, any will do.
Hint: Don't overthink this. A good way to find the shortest is just to sort them.'''

import sys
sys.argv = ["shortest_arg.py", "sakura", "durga", "shyam", "sudan", "sayuri"]
args = sys.argv[1:]

if args:
    shortest=min(args,key=len)
    print(f"The shortest argument is: {shortest}")
else:
    print("Error! please provide some arguements.")
