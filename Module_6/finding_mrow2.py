import numpy as np

# Defining matrix N and P
N = np.array([[1, 2, 0], [0, 1, 1], [2, 0, 1]])
P = np.array([[7, 4, 5], [4, 1, 3], [5, 5, 5]])

# Defining the system of equations
a = N.transpose()
b = P[1]

# Solving the system of equations
m = np.linalg.solve(a, b)

print(m)