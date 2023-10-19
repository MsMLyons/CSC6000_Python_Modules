def add(A, B, op="add"):
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(A[0])):
            if (op == "add"):
                C[-1].append(A[i][j] + B[i][j])
            else:
                C[-1].append(A[i][j] - B[i][j])
    return C

A = [[11, 14], [7, 18], [0, 22]]
B = [[3, 5], [6, -9], [8, -15]]
print("The sum is:", add(A, B))
print("The result of the subtract is:", add(A, B, "sub"))