''' 4.  The Unixwccommand counts the number of lines, words,and characters in a file.
 Write an implementation of this that takes a file name as a command-line
 argument, and then prints the number of lines and characters.
 Note: Linux (and Mac) users can use the "wc" commandto check the results of their
 implementation.'''

import sys
def wc(file_name):
    try:
        with open(file_name, 'r') as f:
            text = f.read()
            lines = text.count('\n') + 1
            chars = len(text)
            print(f"Lines: {lines}, Characters: {chars}")
    except FileNotFoundError:
        print("File not found")

if len(sys.argv) != 2:
    print("Usage: python wc.py <file_name>")
else:
    wc(sys.argv[1])
