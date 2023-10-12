def compute_binomial_coefficient(n, k):
    ans = 1
    if k > n // 2:
        k = n - k
    for i in range(k):
        ans *= (n - i) / (i + 1)
    return int(ans)

def pascals_triangle():
    while True:
        n = int(input("Please enter a number of rows between 4 and 8: "))

        if 4 <= n <= 8:
            break  
        else:
            print("Please enter a valid number of rows.")

    triangle = []  # List to store the rows of Pascal's Triangle

    for row_num in range(n):
        row = []
        for col_num in range(row_num + 1):
            value = compute_binomial_coefficient(row_num, col_num)
            row.append(value)
        triangle.append(row)

    # Printing the Pascal's Triangle with proper formatting
    for row in triangle:
        print(' '.join(f'{value:3}' for value in row).center(n * 4))

pascals_triangle()
