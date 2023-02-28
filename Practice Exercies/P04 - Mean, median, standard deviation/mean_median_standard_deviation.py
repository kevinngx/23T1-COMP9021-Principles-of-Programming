# It computes the mean, the median and the standard deviation of the 
# numbers in the list using nothing but arithmetic operators and displays them as floating point numbers with two digits after the decimal point.

# It computes the mean, the median and the standard deviation of 
# the numbers in the list using the mean(), median() and pstdev() functions from the statistics module and displays them as floating point numbers with two digits after the decimal point.

from random import randrange, seed
from statistics import mean, median, stdev, pstdev
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
    return pstdev(L)

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
print()
print(f'The mean is {get_mean(L):.2f}.')
print(f'The median is {get_median(L):.2f}.')
print(f'The standard deviation is {get_stdev(L):.2f}.')
print()
print('Confirming with functions from the statistics module:')
print(f'The mean is {mean(L):.2f}.')
print(f'The median is {median(L):.2f}.')
print(f'The standard deviation is {pstdev(L):.2f}.')
