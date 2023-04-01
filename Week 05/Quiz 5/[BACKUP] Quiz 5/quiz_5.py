# Written by *** for COMP9021
#
# Uses data available at http://data.worldbank.org/indicator
# on Forest area (% of land area) and Agricultural land area (% of land area).
#
# Prompts the user for two distinct years between 1960 and 2021,
# separated by two consecutive hyphens with possibly spaces before
# and after, as well as a strictly positive integer N,
# and outputs the top N countries where:
# - agricultural land area (as a ratio) has strictly increased from
#   oldest input year to most recent input year;
# - forest area (as a ratio) has strictly increased from oldest input
#   year to most recent input year;
# - the ratio of increase in agricultural land area to
#   increase in forest area (so a ratio of ratio differences)
#   determines output order.
#
# Countries are output from those whose ratio of increases is largest
# to those whose ratio of increases is smallest, as a floating point
# number with 2 digits after the decimal point.
#
# In the unlikely case where many countries share the same ratio
# of increases, countries are output in lexicographic order.
#
# In case fewer than N countries are found, only that number of
# countries is output.
#
# If no country has data for both years, then a special message is output.
#
# The data directory is stored in the working directory.


from collections import defaultdict
import csv
from pathlib import Path
import sys


# INSERT YOUR CODE HERE

range = input('Input two distinct years in the range')


