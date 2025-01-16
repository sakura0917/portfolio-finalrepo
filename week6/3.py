''' 3. Write and test a function that determines if a given integer is a prime number. A
prime number is an integer greater than 1 that cannot be produced by multiplying
two other integers.'''


def is_prime(a):
    factors = []
    for i in range(1, a + 1):
        if a % i == 0:
            factors.append(i)
    if len(factors)==2:
        print (a,"is a prime number")
    else:
        print(a,"is not a prime number")

num=int(input(("enter a number")))
is_prime(num)

