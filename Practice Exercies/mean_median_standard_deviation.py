from random import randrange, seed
from statistics import mean, median, stdev
import sys

MAX_POSSIBLE_VALUE = 50
MIN_POSSIBLE_VALUE = -50

def get_mean(L):
    sum = 0
    for n in L:
        sum = sum + n
    return sum / len(L)

def get_median(L):
    L.sort()
    if len(L) % 2 == 0:
        return (L[int(len(L)/2)-1] + L[int(len(L)/2)])/2
    else:
        return L[int(len(L)/2)]

def get_stdev(L):
    #TODO: Implement stdev without using the in statistics module
    return stdev(L)

try:
    arg_for_seed = int(input('Feed the seed with an integer: '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()

try:
    nb_of_elements = int(input('How many elements do you want to generate? '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()

if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()

seed(arg_for_seed)

L = [randrange(-50, 50) for _ in range(nb_of_elements)]
print('\nThe list is:' , L)

print(f'The mean is {get_mean(L):.2f}')
print(f'The median is {get_median(L):.2f}')
print(f'The standard deviation is {get_stdev(L):.2f}')

print('Confirming with functions from the statistics module')
print(f'The mean is {mean(L):.2f}')
print(f'The median is {median(L):.2f}')
print(f'The standard deviation is {stdev(L):.2f}')