from math import sqrt
from itertools import permutations

def distinct_digits(number):
    observed_digits = {0}
    while number:
        number, digit = divmod(number, 10)
        if digit in observed_digits:
            return False
        observed_digits.update({digit})
    return True

def sieve_of_primes_up_to(n):
    sieve = [False, False] + [True] * (n - 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve

# A number is a good prime if it is prime and consists of nothing but
# distinct nonzero digits.
# Returns True or False depending on whether the integer provided as
# argument is or is not a good prime, respectively.
# Will be tested with for number a positive integer at most equal to
# 50_000_000.
def is_good_prime(number):
    # Step 1 = Check if it is prime --> use the sieve_of_primes_up_to function
    # Step 2 = Check if it is distinct --> define a function distinct_digits(number) using divmod approach
    if sieve_of_primes_up_to(number)[number] and distinct_digits(number):
        return True
    return False

# pattern is expected to be a nonempty string consisting of underscores
# and distinct nonzero digits of length at most 7 (this does not need
# to be checked).
# Underscores have to be replaced by digits so that the resulting number
# is a good prime.
# The function prints out all solutions, if any, from smallest to largest.
def good_primes(pattern):
    # Step 1 find all of the numbers used
    digits_used = set(pattern.replace('_',''))
    # print(digits_used)
    
    # Step 2 create a list of available digits
    available_digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}.difference(digits_used)
    # print(available_digits)
    
    # Step 3 list all permutations of available digits
    perms = permutations(available_digits, pattern.count('_'))
    
    # Step 4 for each permutation, check if the number is a good prime
    g_primes = []    
    for perm in perms:
        pattern_list = list(pattern)
        for digit in perm:
            pattern_list[pattern_list.index('_')] = digit
        number = int(''.join(pattern_list))
        if is_good_prime(number):
            g_primes.append(number)
    
    for prime in sorted(g_primes):
        print(prime)