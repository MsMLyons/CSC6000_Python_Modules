def transpose(A):
    # the transpose of A
    AT = []
    for j in range(len(A[0])):
        # append the j row of AT
        AT.append([])
        for i in range(len(A)):
            AT[-1].append(A[i][j])
    return AT

B = [[11, 14], [7, 18], [0, 22]]
print(B)
print(transpose(B))

C = [[8], [6]]
print(C)
print(transpose(C))
