from random import seed, randrange
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
L = [randrange(19) for _ in range(nb_of_elements)]
# Prints out the list.
print('\nThe list is:' , L)
print()

# kevinngx implementing from below

# Create a dictionary of range + counts
ranges = [{"range":[0,4], "count":0}, {"range":[5,9], "count":0}, {"range":[10,14], "count":0}, {"range":[15,19], "count":0}]

# For each number in the list, check what range it fits into
for n in L:
    for range in ranges:
        if range["range"][0] <= n & n <= range["range"][1]: range["count"] = range["count"] + 1

# Print out, with specific formatting whether the count is 0, 1 or >1
for range in ranges:
    match range["count"]:
        case 0: print(f'There is no element between {range["range"][0]} and {range["range"][1]}.') 
        case 1: print(f'There is {range["count"]} element between {range["range"][0]} and {range["range"][1]}.') 
        case _: print(f'There are {range["count"]} elements between {range["range"][0]} and {range["range"][1]}.') 

