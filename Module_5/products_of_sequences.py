def sequence_product():
    ans = 1
    for i in range(4, 7):
        ans*= i
    return ans
print("The product of sequence 4 to 6 is:", sequence_product())

def product_of_sequence():
    
    begin = eval(input("Please enter a number from 4 - 8 as the beginning of the sequence: "))
    end = eval(input(f"Please enter a number greater than {begin}, but smaller than 9 for the end of the sequence: "))
    
    # add a check for a valid number

    value1 = begin
    value2 = end
    
    ans = 1 

    print(value1, value2)
    for i in range(value1, value2):
        ans *= i
    return ans
    

print("The product of sequence is:", product_of_sequence())
# result --> 
# 4 7
# The product of sequence is: 120 --> range is 4 to 6 (7 - 1, due to indexing)