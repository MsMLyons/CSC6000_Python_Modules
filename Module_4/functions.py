'''Calculate an average'''

def average(a, b):
    return(a + b) / 2

print(average(3, 5))
print()

'''Calculate a ratio - example 1'''

def ratio(c, d):
    if (d == 0):
        return c
    else:
        return c / d

print(ratio(3, 4))
print(ratio(3, 0))
print()

'''Calculate a ratio - example 2'''

def ratio_1(c, d = 1):
    return(c / d)

'''Add separator when printing the result of the ratio'''

print(ratio_1(3, 5), "Wow!", sep = " -- ")
print(ratio_1(3), "I knew it!", sep = " >> ")
print()

'''Decompose number to prime number components'''

def decompose(n):
    primes = []
    for i in range(2, n + 1):
        while n % i == 0:
            primes.append(i)
            n //= i
    return primes

print(decompose(33))
print(decompose(12))
print(decompose(105))
print(decompose(31))
print(decompose(23), "Here we are", sep = " >> ")
print(decompose(59))
print(decompose(121), "Ok, cool", sep = " >> ")
print(decompose(189871))
print(decompose(191161), "I need a radical identity shift", sep = " >> ")
#print(decompose(9876542103), "This takes too long to process", sep = " >> ") 
#print(decompose(31381059607), "IDEM! Is it Halloween yet?", sep = " >> ")
print()

'''Compute the middle pair of two groups'''

def middle_pair(group1, group2):
    pairs = []
    for i in range(len(group1)):
        for j in range(len(group2)):
            pairs.append([group1[i], group2[j]])
    return pairs[len(pairs)//2][0], pairs[len(pairs)//2][1]

group1 = ["A", "B", "C", "D", "E"]
group2 = ["1", "2", "3", "4"]
m1, m2 = middle_pair(group1, group2)
print(m1, "and", m2, "are the middle pairs. *Yay!* *So excited!*")
print()

group1 = ["A", "B", "C", "D"]
group2 = ["1", "2", "3", "4", "5"]
m1, m2 = middle_pair(group1, group2)
print(m1, "and", m2, "are the middle pairs. *Super Cool!* *It works!*")


