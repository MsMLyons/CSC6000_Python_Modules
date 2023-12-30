# Create matrices via user input
def user_matrices():
    print("Let's enter the values for matrix A.")
    rows_A = int(input("Enter the number of rows for matrix A: "))
    columns_A = int(input("Enter the number of columns for matrix A: "))

    # Check if matrix A is square
    while rows_A != columns_A:
        print("Matrix A is not a square matrix. Please re-enter the values.")
        rows_A = int(input("Enter the number of rows for matrix A: "))
        columns_A = int(input("Enter the number of columns for matrix A: "))

    A = []
    for i in range(rows_A):
        row = []
        for j in range(columns_A):
            value = int(input(f"Enter the value for A[{i}][{j}]: "))
            row.append(value)
        A.append(row)
    print()

    print("Now let's enter the values for matrix B.")
    rows_B = int(input("Please enter the number of rows for matrix B: "))
    columns_B = int(input("Please enter the number of columns for matrix B: "))

    # Check if matrix B is square
    while rows_B != columns_B:
        print("Matrix B is not a square matrix. Please re-enter the values.")
        rows_B = int(input("Enter the number of rows for matrix B: "))
        columns_B = int(input("Enter the number of columns for matrix B: "))

    B = []
    for i in range(rows_B):
        row = []
        for j in range(columns_B):
            value = int(input(f"Enter the value for B[{i}][{j}]: "))
            row.append(value)
        B.append(row)

    return A, B

A, B = user_matrices()

print()

# Print the matrices to visualize them
print(f"Matrix A is {A} and matrix B is {B}.")

# Multiply the matrices to help establish if they are inverses of each other
def mult(A, B):
    # Check if the number of columns in A is equal to the number of columns in B
    if len(A[0]) != len(B):
        print("The matrices are not compatible for multiplication.")
        return None

    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(B[0])):
            temp = 0
            for k in range(len(B)):
                temp += A[i][k] * B[k][j]
            C[-1].append(temp)
    return C

# Generate the identity matrix for each matrix
def generate_ID_matrix(rows, columns):
    identity_matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        identity_matrix.append(row)
    return identity_matrix

# Check to see if each matrix is the inverse of the other
def is_inverse(A, B):

    AB = mult(A, B)
    if AB is None:
        return False
    rows_AB = len(AB)
    columns_AB = len(AB[0])
    identity_AB = generate_ID_matrix(rows_AB, columns_AB)
    if AB == identity_AB:
        return True
    
    BA = mult(B, A)
    if BA is None:
        return False
    rows_BA = len(BA)
    columns_BA = len(BA[0])
    identity_BA = generate_ID_matrix(rows_BA, columns_BA)
    if BA == identity_BA:
        return True
    
    return False

# Print the correct message regarding whether the matrices are the inverse of each other
if is_inverse(A, B):
    print("The matrices are the inverse of each other.")
else:
    print("The matrices are not the inverse of each other.")