# Written by *** for COMP9021

# Prompts the user for a seed, a dimension dim, and an upper bound N.
# Randomly fills a grid of size dim x dim with numbers between 0 and N
# and computes:
# - the largest value n such that there is a path of the form (0, 1, 2,... n);
# - the number of such paths.
# A path is obtained by repeatedly moving in the grid one step north, south,
# west, or east.


import sys
from random import seed, randint


def display_grid():
    for row in grid:
        print(' '.join(f'{e:{len(str(upper_bound))}}' for e in row)) 

def value_and_number_of_longest_paths():
    return 0, 0
    # REPLACE THE RETURN STATEMENT WITH YOUR CODE        

# POSSIBLY DEFINE OTHER FUNCTIONS

try:
    for_seed, dim, upper_bound = (abs(int(x)) for x in
                                     input('Enter three integers: ').split()
                                 )
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randint(0, upper_bound) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()

max_value, nb_of_paths_of_max_value = value_and_number_of_longest_paths()
if not nb_of_paths_of_max_value:
    print('There is no 0 in the grid.')
else:
    print('The longest paths made up of consecutive numbers starting '
          f'from 0 go up to {max_value}.'
         )
    if nb_of_paths_of_max_value == 1:
        print('There is one such path.')
    else:
        print('There are', nb_of_paths_of_max_value, 'such paths.')
