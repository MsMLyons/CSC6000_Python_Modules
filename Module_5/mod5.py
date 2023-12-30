# calculate the binomial coefficient 
def comb(n, k):
    ans = 1
    if k > n // 2:
        k = n - k
    for i in range(k):
        ans *= (n - i) / (i + 1)
    return int(ans)

# formulate the output of Pascal's triangle, based on user input & invoking the comb function
def pascals_triangle():

    while True:

        # ask for the number of rows
        n = int(input("Please enter a number of rows between 4 and 8: "))  

        # if the number of rows is not within the expected parameters, re-prompt
        if 4 <= n <= 8:            
            break
        else:
            print("Please enter a valid number of rows.")

    # create a variable to store the row lists & initiate as empty list
    # will be a list of lists once row lists are appended
    triangle = []

    # loop through the possible row numbers 
    # generate their values to store in the row lists & triangle list
    # r, c --> variables for row number, column number
    for r in range(n):
        row = []
        for c in range(r + 1):
            value = comb(r, c)
            row.append(value)
        triangle.append(row)

    # create spacing, format & print the values of each row
    spacing = n - 1

    for row in triangle:
        # print()
        print('  ' * spacing, end=' ')
        for value in row:
            print("{:^3}".format(value), end='  ')
        print()
        spacing -= 1

pascals_triangle()