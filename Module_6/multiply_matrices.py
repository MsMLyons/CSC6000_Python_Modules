def mult(A, B):
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(B[0])):
            temp = 0
            for k in range(len(B)):
                temp += A[i][k] * B[k][j]
            C[-1].append(temp)
    return C

A = [[10, 20], [30, 40], [50, 60]]
B = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(mult(A, B))