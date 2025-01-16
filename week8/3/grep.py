''' 3. The Unixgrepcommand searches a file and outputsthe lines in the file that
 contain a certain pattern. Write an implementation of this. It will take two
 command-line arguments: the first is the string to look for, and the second is the
 file name. The output should be the lines in the file that contain the string.'''

import sys

def grep(pattern, file_name):
    try:
        with open(file_name, 'r') as f:
            for line in f:
                if pattern in line:
                    print(line, end='')
    except FileNotFoundError:
        print("File not found")

if len(sys.argv) != 3:
    print("Usage: python grep.py <pattern> <file_name>")
else:
    grep(sys.argv[1], sys.argv[2])
