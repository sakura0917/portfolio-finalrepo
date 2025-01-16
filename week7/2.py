'''2.	Write and test three functions that each take two words (strings) as 
parameters and return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.
Hint: These could all be done programmatically, but consider carefully what
 topic we have been discussing this week!
 Each function can be exactly one line.
'''
def unique_letters(word1, word2):
    return sorted(set(word1)|set(word2))

def common_letters(word1, word2):
    return sorted(set(word1)&set(word2))

def different_letters(word1, word2):
    return sorted(set(word1)^set(word2))

word1 = "cheese"
word2 = "seeds"

print(unique_letters(word1, word2))
print(common_letters(word1, word2))
print(different_letters(word1, word2))
