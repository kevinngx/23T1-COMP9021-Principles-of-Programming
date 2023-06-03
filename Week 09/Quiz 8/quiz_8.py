# Written by *** for COMP9021
#
# Creates 3 classes, Point, Line and Parallelogram.
# A point is determined by 2 coordinates (int or float).
# A line is determined by 2 distinct points.
# A parallelogram is determined by 4 distinct lines,
# two of which have the same slope, the other two
# having the same slope too, but different to the other one.
# The Parallelogram class has a method, divides_into_two_parallelograms(),
# that determines whether a line, provided as argument, can split
# the object into two smaller parallelograms.


from collections import defaultdict


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

# Define a class to raise Line errors


class Line:
    pass
    # Replace pass above with your code


# Define a class to raise Parallelogram errors


class Parallelogram:
    pass
    # Replace pass above with your code

    def divides_into_two_parallelograms(self, line):
        return
        # Replace the return statement above with your code
        
