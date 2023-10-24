import statistics
import math

# If the number of data points is odd, all three functions return the middle value directly.
# If the number of data points is even, 
# statistics.median() returns the arithmetic mean of the two middle values, 
# statistics.median_low() returns the smaller value, 
# and statistics.median_high() returns the larger value.

def find_median():
    x = [3, 1, 8, 7]
    print("This is the median of the values in the list: ", statistics.median(x))
    print("This is the smallest median value in the list: ", statistics.median_low(x))
    print("This is the largest median value in the list: ", statistics.median_high(x))

find_median()

# sample output: 
# This is the median of the values in the list 5.0
# This is the smallest median value in the list 3
# This is the largest median value in the list 7