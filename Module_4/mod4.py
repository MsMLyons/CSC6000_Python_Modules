# Solving Arrangements of Multisets
# Write a Python program to compute Arrangements of Multisets

def arrange_multiset():
    while True:
        # ask the user for the number of subsets
        j = eval(input("Please enter a number of subsets no smaller than 3 and no greater than 8: "))
    
        if (j < 3 or j > 8):
            print("Please follow instructions and try again.")
            continue
            
        subset_sizes = []
        
        # subsets mi go from 1 to j
        for i in range(1, j + 1):
            while True:
                # ask for the size of each subset
                m = eval(input("Please enter the size of the subset, from 1 to 5: "))

                if (m >= 1 and m <= 5):
                    subset_sizes.append(m)
                    break
                else:
                    print("That is not a valid subset size. Please try again.")                     
        # visualize subset sizes chosen (not a required feature)     
        print("These are the subset sizes: ", subset_sizes)

        n = sum(subset_sizes)
                
        while True:
            # ask for the number of arrangements; prompt based on requirement it be smaller than the sum of the subset sizes  
            k = eval(input(f"Please enter the number of arrangements. It must be smaller than {n}, the sum of the subset sizes: "))
        
            if (k < n):
                # Compute the number of arrangements of k elements out of n, considering the subsets of size mi
                acc = 1
                for i in range(n, n-k, -1):
                    acc *= i
                print(f"Given your inputs, the number of arrangements is {acc}.")                
                break  
            else:
                print("That is not a valid number of arrangements. Try again.")                

        break
                    
arrange_multiset()      