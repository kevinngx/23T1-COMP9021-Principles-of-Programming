# Written by Eric Martin for COMP9021


'''
Recursive solution to the Tower of Hanoi puzzle.
'''


def move_towers(n, start_position, end_position, extra_position):
    '''
    Move a tower of n disks from start_position to end_position,
    with extra_position available.

    >>> move_towers(4, 0, 2, 1)
    Move disk of size 1 from position 0 to position 1
    Move disk of size 2 from position 0 to position 2
    Move disk of size 1 from position 1 to position 2
    Move disk of size 3 from position 0 to position 1
    Move disk of size 1 from position 2 to position 0
    Move disk of size 2 from position 2 to position 1
    Move disk of size 1 from position 0 to position 1
    Move disk of size 4 from position 0 to position 2
    Move disk of size 1 from position 1 to position 2
    Move disk of size 2 from position 1 to position 0
    Move disk of size 1 from position 2 to position 0
    Move disk of size 3 from position 1 to position 2
    Move disk of size 1 from position 0 to position 1
    Move disk of size 2 from position 0 to position 2
    Move disk of size 1 from position 1 to position 2
    '''
    if n > 1:
        move_towers(n - 1, start_position, extra_position, end_position)
    print('Move disk of size', n, 'from position', start_position,
          'to position', end_position
         )
    if n > 1:
        move_towers(n - 1, extra_position, end_position, start_position)



if __name__ == '__main__':
    import doctest
    doctest.testmod()
