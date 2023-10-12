def scale(A, s):
    As = []
    for i in range(len(A)):
        As.append([])
        for j in range(len(A[i])):
            As[i].append(A[i][j] * s)
    return As

A = [[11, 14], [7, 18], [0, 22]]
print("This is scale A, 10:", scale(A, 10))
B = [[8], [6]]
print("This is scale B, 0.5:", scale(B, 0.5))