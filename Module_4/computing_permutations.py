# Computing permutations

# P(n) = n!

def permutation(n):
    acc = 1
    for i in range(2, n + 1):
        acc *= i
    return acc

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 20, 50]:
    print("Permutation of {:2} is {}".format(i, permutation(i)))

# result -->
# Permutation of  1 is 1
# Permutation of  2 is 2
# Permutation of  3 is 6
# Permutation of  4 is 24
# Permutation of  5 is 120
# Permutation of  6 is 720
# Permutation of  7 is 5040
# Permutation of  8 is 40320
# Permutation of  9 is 362880
# Permutation of 11 is 39916800
# Permutation of 12 is 479001600
# Permutation of 13 is 6227020800
# Permutation of 14 is 87178291200
# Permutation of 15 is 1307674368000
# Permutation of 20 is 2432902008176640000
# Permutation of 50 is 30414093201713378043612608166064768844377641568960512000000000000