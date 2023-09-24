# Sequences

print(list(range(1, 5)), end='\n\n')

# prints [1, 2, 3, 4]

print(list(range(2, 10, 2)), end='\n\n')

# prints [2, 4, 6, 8]

print(list(range(14, 0, -4)), end='\n\n')

# prints [14, 10, 6, 2]

# Progressions

for i in range(15, 0, -5):
    print(i)

# prints 
# 15, 10, 5 (but not in list format with brackets)

for i in range(100, 110):
    print(i)

# prints 100 - 109, incrementing by 1 each time

for i in range(1000, 880, -10):
    print(i)

# prints backwards from 1000 - 880, subtracting by 10 each time

for i in range(5605, 5724, 17):
    print(i)

# prints from 5605 - 5724, adding 17 each time