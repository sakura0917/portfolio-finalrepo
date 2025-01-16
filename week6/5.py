''' 5. Another way to hide a message is to include the letters that make it up within
seemingly random text. The letters of the message might be every fi h character,
for example. Write and test a function that does such encryption. It should
randomly generate an interval (between 2 and 20), space the message out
accordingly, and should fill the gaps with random letters. The function should
return the encrypted message and the interval used.
For example, if the message is "send cheese", the random interval is 2, and for
clarity the random letters are not random:
send cheese
s  e  n  d   c  h  e  e  s  e
sxyexynxydxy cxyhxyexyexysxye'''

import random
import string
def encrypt_with_random_interval(message):
    interval = random.randint(2, 20) 
    encrypted_message = ''.join(
        char + (random.choice(string.ascii_letters) if (i + 1) % interval == 0 and i != len(message) - 1 else '')
        for i, char in enumerate(message)
    )
    return encrypted_message, interval
message = "send cheese"
encrypted, interval = encrypt_with_random_interval(message)
print(f"Original message: {message}")
print(f"Encrypted message: {encrypted}")
print(f"Interval used: {interval}")
