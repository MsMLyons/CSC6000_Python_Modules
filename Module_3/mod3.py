# Step 1: Define a function to:
    # calculate geometric progression, 
    # print the sum of elements, 
    # and print the first 3 elements in the progression 
# Step 2: Request a scale factor and common ratio from the user
# Step 3: Inform the user if the GP converges to a sum regardless of the number of elements
# Step 4: If so, compute the sum of infinite elements
# Step 5: If not, request the number of elements in the geometric progression
# Step 6: Check if r is equal to 1 or -1; if so, compute the sum of the elements
# Step 7: Otherwise, if r is is not equal to a number already tested, compute the sum of all elements
# Step 8: Print the first 3 elements in the geometric progression
# Step 9: Call the function

def gp_sum():

    a = eval(input("Please enter a scale factor: ")) 
    r = eval(input("Please enter a common ratio: "))

    if (r > -1) and (r < 1):
        print("This GP converges with infinite elements to", a / (1 - r))
    else:
        n = eval(input("Please enter the number of elements: ")) 
        if (r == 1):        
            print("The sum is", a * n)
        elif (r == -1):
            if (n % 2 == 1 ):
                print("The sum is", a)     
            else:
                print("The sum is", 0)
        else:
            print("This GP does not coverge to a finite number with infinite elements")
            sum = a * (r ** n - 1) / (r - 1)
            print(f"This GP sum with {n} elements is equal to", sum)

    print("The first three elements are:", a, a * r, a * r * r)

gp_sum()