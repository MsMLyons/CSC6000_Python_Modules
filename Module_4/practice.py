def arrange_multiset():
    #use a while loop here
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
        #print(f"The number of arrangements is {k}")

        #compute the number of arrangements of k elements out of n
        #above works; problem from the arrangement function - see mod4.py for modification
                       
        if (k < n):
            print(f"The number of arrangements equals {k}, which is less than the sum of the subsets, which equals {n}")
            acc = 1
            for i in range(n, n-k, -1):
                acc *= i
            
            print("Given your inputs, the number of arrangements is {}.".format(arrangement(n, k)))                
            break
        else:
            print("That is not a valid number of arrangements. Try again.")        
            break
                    
            
arrange_multiset()
            
            

   
    

   




        
        

# ○ Asks the user the size of each subset (from 1 to 5);

# ■ mi        with i going from 1 to j

# ○ Asks the user the total number of the arrangements (a number smaller than the sum of sizes of the subsets - n)
# n will equal the sum of the elements of each subset
# ■ k

# ○ Then, it computes and prints the number of arrangements of k elements out of n, considering the subsets of size mi;

# slide 25 vs slide 31
#def fact(n):
    #ans = 1
    #for i in range(2, n + 1):
        #ans *= i
    #return ans

#def perm_rep(mj):
    #n = 0
    #divisor = 1
    #for mi in mj:
        #n += mi
        #divisor *= fact(mi)
    #return fact(n) // divisor
