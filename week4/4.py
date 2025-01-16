''' When processing data it is o en useful to remove the last character from some
 input (it is o en a newline). Write and test a function that takes a string parameter
 and returns it with the last character removed. (If the string contains one or fewer
 characters, return it unchanged.)'''

def test(name):
    newName=""
    if len(name)<=1:
        print("the word you entered doesnot have enough characters, so result= ",name)
    else:
        for x in range(len(name)-1):
            newName+=name[x]
        print("result=", newName)
word=input("enter a word")
test(word)