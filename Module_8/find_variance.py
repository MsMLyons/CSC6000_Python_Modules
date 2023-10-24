import statistics
import math

def find_variance():
    x = [10, 1, 3, 7, 1]
    print("This is the population variance of list x: ", statistics.pvariance(x))
    print("This is the sample variance of list x: ", statistics.variance(x))
    print()

    # quiz question 10
    y = [4, 6, 6, 7, 7]
    print("This is the population variance of list y: ", statistics.pvariance(y))
    print("This is the sample variance of list y: ", statistics.variance(y))
    print()

    #quiz question 4
    z = [5, 4, 3, 4]
    print("This is the population variance of list y: ", statistics.pvariance(z))
    print("This is the sample variance of list y: ", statistics.variance(z))
    print()

find_variance()

# sample output:
# This is the population variance of list x:  12.64
# This is the sample variance of list x:  15.8

# This is the population variance of list y:  1.2
# This is the sample variance of list y:  1.5

# statistics.pvariance() computes the population variance, 
# which is the appropriate measure when the data represents 
# the entire population.

# statistics.variance() computes the sample variance, 
# which is the appropriate measure when the data is 
# a sample from a larger population.

# source: https://note.nkmk.me/en/python-statistics-mean-median-mode-var-stdev/ 