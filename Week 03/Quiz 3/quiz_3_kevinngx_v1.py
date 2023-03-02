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

# Putting it all together
direction_mapping = {'0': '⇩', '1': '⬃', '2': '⬂'}

def convert_to_base_three(n):
    if n == 0: return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
        result = ''.join(reversed(nums))
    return result

def print_direction_string(directions):
    for direction in directions:
        print(direction_mapping[direction], end='')
        
def print_line(position, direction):
    print(' '*position, direction_mapping[direction], sep='')
    if direction == '1': 
        return -1
    elif direction == '2': 
        return 1
    elif direction == '0': return 0

    
def get_initial_position(directions):
    position = 0
    min_position = 0
    for direction in directions:
        if direction == '1': 
            position += -1
        elif direction == '2': 
            position += 1
        elif direction == '0': 
            position += 0
        min_position = min(position, min_position)
    if min_position < 0:
        return abs(min_position)
    else:
        return 0
    
directions = convert_to_base_three(encoded_directions)
print(f'In base 3, the input reads as: {directions}')
print()
print(f'So that\'s how you want to go: ', end='')
print_direction_string(directions)
print()
print()
print('Let\'s go then!')
position = get_initial_position(directions)
for direction in directions:
    position += print_line(position, direction)
    if position < 0: position = 0
