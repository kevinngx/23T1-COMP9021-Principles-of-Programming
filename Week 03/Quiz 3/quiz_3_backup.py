# Written by *** for COMP9021

# Prompts the user for a positive integer.
# - When written in base 3, its consecutive digits read
#   from left to right represent the directions to take, with
#   * 0 meaning going South,
#   * 1 meaning South West,
#   * 2 meaning South East.
#
# Prints out:
# - the representation of the second digit in base 3;
# - the corresponding sequence of directions to take, as arrows;
# - the sequence of arrows again, but nicely displayed.
#
# The leftmost arrow is printed out with no space to the left.
#
# The arrows are the Unicode characters of code point
# 0x21e9 and 0x2b02 and 0x2b03.

import sys

try:
    encoded_directions = int(input('Enter a positive integer: '))
    if encoded_directions < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

# INSERT YOUR CODE HERE
