def arrangement(n, k):
    acc = 1
    for i in range(n, n-k, -1):
        acc *= i
    return acc

def arrange_multiset():
    while True:
        j = eval(input("Please enter a number of subsets (no smaller than 3, no greater than 8): "))
    
        if (j < 3 or j > 8):
            print("Please follow instructions and try again.")            
            
        else:
            if (j >= 3 or j<= 8):
                subset_sizes = []
        
                for i in range(1, j + 1):
                    while True:
                         m = eval(input("Please enter the size of the subset, from 1 to 5: "))

                         if (m >= 1 and m <= 5):
                            subset_sizes.append(m)
                            break
                         else:
                            print("That is not a valid subset size. Please try again.")                     
                        
            else:
                break
                
        print("These are the subset sizes: ", subset_sizes)

        n = sum(subset_sizes)
        print(f"The sum of the subset sizes equals {n}.")

        k = eval(input(f"Please enter the number of arrangements. It must be smaller than {n}: "))
                              
        if (k < n):
            # Call the arrangement function and print the result
            print("Given your inputs, the number of arrangements is {}.".format(arrangement(n, k)))                
            break
        else:
            print("That is not a valid number of arrangements. Try again.")        
            break
                    
arrange_multiset()
