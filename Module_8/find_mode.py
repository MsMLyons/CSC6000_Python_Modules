import statistics
import math

# If multiple modes exist, statistics.mode() returns the first one.
# To return multiple modes, use statistics.multimode() instead

def find_mode():
    x = [3, 2, 3, 2, 1, 2]
    print("This is the mode of the values in the list: ", statistics.mode(x))
    print("This is the multimode of the values in the list, printed in list format: ", statistics.multimode(x))

find_mode()    

# sample output: 
# This is the mode of the values in the list:  2
# This is the multimode of the values in the list, printed in list format:  [2]