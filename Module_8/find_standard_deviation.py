import statistics
import math

def find_standard_deviation():
    x = [10, 1, 3, 7, 1]

    # statistics.pstdev() returns the population standard deviation.
    print("This is the value for population standard deviation: ", statistics.pstdev(x))

    # The population standard deviation is the square root of the population variance.
    print("This is the value for the square root of the population variance: ", math.sqrt(statistics.pvariance(x)))
    print("This is equal to the population standard deviation")
    if statistics.pstdev(x) == math.sqrt(statistics.pvariance(x)):
        print("Hooray!")
    else:
        print("Boo")
    print()

    # statistics.stdev() returns the sample standard deviation.
    print("This is the value for the sample standard deviation: ", statistics.stdev(x))

    # The sample standard deviation is the square root of the sample variance.
    print("This is the value for the square root of the sample variance: ", math.sqrt(statistics.variance(x)))
    print("This is equal to the sample standard deviation")
    if statistics.stdev(x) == math.sqrt(statistics.variance(x)):
        print("Yay!")
    else:
        print("Ugh")

find_standard_deviation()

# sample output: 
