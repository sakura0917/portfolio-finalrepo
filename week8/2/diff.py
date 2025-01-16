''' 2.  The Unixdiffcommand compares two files and reportsthe differences, if any.
 Write a simple implementation of this that takes two file names as command-line
 arguments and reports whether or not the two files are the same. (Define "same" as
 having the same contents.)'''

import sys
def diff(f1, f2):
    try:
        with open(f1, 'r') as a, open(f2, 'r') as b:
            print("Same" if a.read() == b.read() else "Different")
    except FileNotFoundError:
        print("File not found")

if len(sys.argv) != 3:
    print("Usage: python diff.py <file1> <file2>")
else:
    diff(sys.argv[1], sys.argv[2])
