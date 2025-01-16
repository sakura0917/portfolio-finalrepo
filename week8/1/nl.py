'''1. The Unixnlcommand prints the lines of a text filewith a line number at the start
 of each line. (It can be useful when printing out programs for dry runs or white-box
 testing). Write an implementation of this command. It should take the name of the
 files as a command-line argument.'''

import sys
def number_lines(file_name):
    try:
        with open(file_name, 'r') as f:
            for num, line in enumerate(f, start=1):
                print(f"{num}\t{line}", end='')
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")

if len(sys.argv) != 2:
    print("Usage: python nl.py <file_name>")
else:
    file_name = sys.argv[1]
    number_lines(file_name)

