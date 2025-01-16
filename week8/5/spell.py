''' 5.  The Unixspellcommand is a simple spell-checker.It prints out all the words in a
 text file that are not found in a dictionary. Write and test an implementation of this,
 that takes a file name as a command-line argument.
 Note: You may want to simplify the program at first by testing with a text file that
 does not contain any punctuation. A complete version should obviously be able to
 handle normal files, with punctuation.
 Another Note: You will need a list of valid words. Linux users will already have one
 (probably in /usr/share/dict/words). It is more complicated,as usual, for
 Windows users. Happily, there are several available on GitHub.'''

import sys

def load_dictionary(dict_file):
    try:
        with open(dict_file, 'r') as f:
            return set(word.strip().lower() for word in f)
    except FileNotFoundError:
        print("Dictionary file not found")
        sys.exit(1)

def spell_check(file_name, dictionary):
    try:
        with open(file_name, 'r') as f:
            words = f.read().lower().split()
            unknown = {word.strip(".,!?()") for word in words if word.strip(".,!?()") not in dictionary}
            print("\n".join(unknown) if unknown else "No spelling errors found")
    except FileNotFoundError:
        print("File not found")

if len(sys.argv) != 3:
    print("Usage: python spell.py <text_file> <dictionary_file>")
else:
    dictionary = load_dictionary(sys.argv[2])
    spell_check(sys.argv[1], dictionary)
