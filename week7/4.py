'''4.One approach to analysing some encrypted data where a substitution is suspected is frequency analysis.
 A count of the different symbols in the message can be used to identify the language used, and sometimes some of the letters.
In English, the most common letter is "e", and so the symbol representing "e" should appear most in the encrypted text.
Write a program that processes a string representing a message and reports the six most common letters, along with the number of times they appear. 
Case should not matter, so "E" and "e" are considered the same.
Hint: There are many ways to do this. It is obviously a dictionary, but we will want zero counts, so some initialisation is needed. Also, sorting 
dictionaries is tricky, so best to ignore that initially, and then check the usual resources for the runes.
'''
def count_letters(message):
    counts = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

    for char in message.lower():
        if char.isalpha():
            counts[char] += 1

    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:6]

    return sorted_counts

message = input("Enter the message: ")
result = count_letters(message)

for letter, count in result:
    print(f"Letter: {letter.upper()} - Count: {count}")
