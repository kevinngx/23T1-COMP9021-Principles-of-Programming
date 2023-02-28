# %load max_in_list.py
# Written by Eric Martin for COMP9021


from random import seed, randint
import sys


# Prompts the user for an integer to provide as argument to the
# seed() function.
try:
    arg_for_seed = int(input('Feed the seed with an integer: '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()   
# Prompts the user a strictly positive number, nb_of_elements.
try:
    nb_of_elements = int(input('How many elements do you want to generate? '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()
seed(arg_for_seed)
# Generates a list of nb_of_elements random integers between 0 and 99.
L = [randint(0, 99) for _ in range(nb_of_elements)]
# Prints out the list.
print('\nThe list is:', L)
# Computes the maximum element of the list without using the
# builtin max().
max_element = 0
min_element = 99
for e in L:
    if e > max_element:
        max_element = e
    if e < min_element:
        min_element = e

# print('\nThe maximum number in this list is:', max_element)
# print('\nThe minimum number in this list is:', min_element)
print(f'\nThe maximum difference between largest and smallest values in this list is: {max_element - min_element}')
print(f'Confirming with builtin operations: {max(L) - min(L)}')


