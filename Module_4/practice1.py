def arrange_multiset():
    while True:
        j = eval(input("Please enter a number of subsets not smaller than 3 and no greater than 8:"))
        if (j < 3 or j > 8):
            print("Please enter a valid number of subsets")
            
        else:
            print(f"Thank you. You have entered {j} subsets")
            break

    while True:
        #subsets = j
        subset_sizes =[]
        for i in range(j, j + 1):
            m = eval(input("Please enter the size of the subset, from 1 to 5: "))
            if (m >= 1 or m <= 5):
                subset_sizes.append(m)
                print(list(subset_sizes))
                break
            else:
                print("That is not a valid subset size. Please try again.")
                
                
arrange_multiset()
print("So far, so good")
