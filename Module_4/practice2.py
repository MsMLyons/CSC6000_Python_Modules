def arrange_multiset():
    j = 0
    while j < 3 or 8 < j:
        j = eval(input("Please enter a number from 3 to 8: "))
    if (3 <= j <= 8):
        subset_size = []
        for i in range(1, j + 1):
            m = eval(input("Please enter a number from 1 to 5: "))
            if (1 <= m <= 5):
                subset_size.append(m)
            else: print("Please enter a valid number from 1 to 5.")
        print("The list of values is: ", subset_size)
    else:
        print("Please enter a valid number of subsets.")

arrange_multiset()
print("This worked")