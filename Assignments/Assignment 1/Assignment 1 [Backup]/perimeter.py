import sys


# INSERT YOUR OWN FUNCTIONS

filename = input('Which data file do you want to use? ')
try:
    with open(filename) as file:
        pass
        # REPLACE PASS ABOVE WITH YOUR CODE
except FileNotFoundError:
    print('Could not open a file named', filename)
    print('Giving up...')
    sys.exit()
