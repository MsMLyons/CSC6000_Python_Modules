def matrix_input(m, n):
    a = []
    for i in range(m):
        b = []
        for j in range(n):
            j = int(input("Please enter a number in the brackets ["+str(i)+"] ["+str(j)+"]: "))
            b.append(j)
        a.append(b)
    return a

def print_matrix(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            print(a[i][j], end = "     ")
        print()

m = int(input("Enter the number of rows in the matrix: "))
n = int(input("Enter the number of columns in the matrix: "))
a = matrix_input(m, n)
print("The matrix is: ")
print_matrix(a)