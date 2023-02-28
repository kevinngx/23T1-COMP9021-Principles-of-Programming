# Write a program characters_triangle.py that prompts the user for a strictly positive integer n and outputs a triangle of height n as shown in the tests.

height = int(input('Enter a strictly positive integer: '))

def get_char_int(char):
    return (char-65)%26 + 65

char = 65
middle = 65

for row in range(height + 1):
    char = middle
    print(" "*(height-row), end='')
    for letter in range(row):
        print(chr(get_char_int(char)), end='')
        char = char + 1
    middle = char
    char = char - 2
    for letter in range(row - 1):
        print(chr(get_char_int(char)), end='')
        char = char - 1
    print('')
