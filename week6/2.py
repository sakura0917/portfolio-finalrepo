''' 2. Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by another to
yield the original).'''

#Python function that takes an integer as its parameter and returns a list of its factors.
def find_factors(a):
    if a <= 0:
        print("Please enter a positive number.")
    factors = []
    for i in range(1, a + 1):
        if a % i == 0:
            factors.append(i)
    
    return factors


num = 64
factors = find_factors(num)
print(f"The factors of {num} are: {factors}.")
