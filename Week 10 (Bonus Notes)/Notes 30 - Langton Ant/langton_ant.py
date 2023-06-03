# Written by Eric Martin for COMP9021


from collections import defaultdict
import sys

import pygame


RED = 255, 0, 0
GREEN = 0, 255, 0
WHITE = 255, 255, 255
dim = 200
cell_side_length = 5
locations = defaultdict(lambda: -1j)
# Ant at the centre of pygame window to start with.
position = complex(dim, dim)
# Ant looking West to start with, so that taking a right turn,
# it first moves North.
direction = -cell_side_length
# Number of frames by second when corresponding key
# (the digits from 1 up to 9) is pressed.
keys_for_frames = {pygame.K_1: 1, pygame.K_2: 2, pygame.K_3: 4, pygame.K_4: 10,
                   pygame.K_5: 20, pygame.K_6: 30, pygame.K_7: 40,
                   pygame.K_8: 50, pygame.K_9: 60
                  }                                
colours = {-1j: RED, 1j: WHITE}       
pygame.init()
screen = pygame.display.set_mode((2 * dim + cell_side_length,
                                  2 * dim + cell_side_length
                                 )
                                )
pygame.display.set_caption('Langton ant')
screen.fill(WHITE)
clock = pygame.time.Clock()
frames_per_second = 1
x, y = int(position.real), int(position.imag)
# Drawing ant at initial position.
pygame.draw.rect(screen, GREEN, (x, y, cell_side_length, cell_side_length), 0)
pygame.display.update()
while True:
    clock.tick(frames_per_second)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # LeftShift-Q to quit.
            if pygame.key.get_mods() == pygame.KMOD_LSHIFT\
               and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key in keys_for_frames:
                frames_per_second = keys_for_frames[event.key]
    # When the ant is on this cell for the first time,
    # locations[position] is -j, and as the ant is about to leave
    # this cell, the cell colour has to change from white to red.
    # In any case, as the ant is about to leave this cell, the cell
    # colour has to change.
    pygame.draw.rect(screen, colours[locations[position]],
                     (x, y, cell_side_length, cell_side_length)
                    )
    locations[position] *= -1
    # If the cell was white, the cell colour was changed to red and the
    # previous assignment switched locations[position] from -j to j;
    # the ant has to take a right turn which, as the y axis is
    # pointing South, is obtained by multiplying direction by j.
    # Otherwise, locations[position] is now -j and the ant has to
    # take a left turn, which is obtained by multiplying direction by
    # -j.
    direction *= locations[position]
    position += direction
    x, y = int(position.real), int(position.imag)
    # Drawing ant at new position.
    pygame.draw.rect(screen, GREEN, (x, y, cell_side_length, cell_side_length))
    pygame.display.update()
