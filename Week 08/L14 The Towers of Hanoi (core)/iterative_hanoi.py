# Written by Eric Martin for COMP9021


'''
Iterative solution to the towers of Hanoi puzzle.
'''


def move_towers(n, start_position, end_position, extra_position):
    '''
    Move a tower of n disks from start_position to end_position,
    with extra_position available.

    >>> move_towers(4, 0, 2, 1)
    Move smallest disk from position 0 to position 1
    Move disk of size 2 from position 0 to position 2
    Move smallest disk from position 1 to position 2
    Move disk of size 3 from position 0 to position 1
    Move smallest disk from position 2 to position 0
    Move disk of size 2 from position 2 to position 1
    Move smallest disk from position 0 to position 1
    Move disk of size 4 from position 0 to position 2
    Move smallest disk from position 1 to position 2
    Move disk of size 2 from position 1 to position 0
    Move smallest disk from position 2 to position 0
    Move disk of size 3 from position 1 to position 2
    Move smallest disk from position 0 to position 1
    Move disk of size 2 from position 0 to position 2
    Move smallest disk from position 1 to position 2
    '''
    direction = -1 if n % 2 else 1
    stacks = list(range(n, 0, -1)), [], []
    small_disk_pos = 0
    for i in range(2 ** n - 1):
        if i % 2 == 0:
            new_small_disk_pos = (small_disk_pos + direction) % 3
            print('Move smallest disk from position', small_disk_pos,
                  'to position', new_small_disk_pos
                 )
            stacks[new_small_disk_pos].append(stacks[small_disk_pos].pop())
            small_disk_pos = new_small_disk_pos
        else:
            from_pos, to_pos =\
                      (small_disk_pos + 1) % 3, (small_disk_pos + 2) % 3
            if not stacks[from_pos] or\
               stacks[to_pos] and stacks[to_pos][-1] < stacks[from_pos][-1]:
                from_pos, to_pos = to_pos, from_pos
            print('Move disk of size', stacks[from_pos][-1],
                  'from position', from_pos, 'to position', to_pos
                 )
            stacks[to_pos].append(stacks[from_pos].pop())


if __name__ == '__main__':
    import doctest
    doctest.testmod()
