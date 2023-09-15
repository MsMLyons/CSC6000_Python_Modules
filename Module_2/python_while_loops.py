v = 0
while(v < 10):
    print(v)
    v +=1
# result --> prints 0 - 9


for v in range(10):
    print(v)
# result --> also prints 0 - 9


a = [3, 8, 2, 0, 7, 5]
for i in range(len(a)):
    if (a[i] == 0):
        break
    else: print(a[i])
# result --> prints the items in a [3, 8, 2]; stops printing when a[i] == 0


c = [4, 8, 2, 0, 7, 5]
i = 0
while(i < len(c)) and (c[i] != 0):
#while(i < len(c)):
    print(c[i], "wow")
    # result --> continuously prints the first number in the array; why?
    # add the following to increment i and to keep the loop from executing forever
    i += 1
# result --> after adding the i += 1 to the code, it prints 4, 8, 2 & wow


d = [5, 7, 2, 0, 3, 8]
i = 0
while(i < len(d)):
    if d[i] == 0:
        break
    print(d[i])
    i += 1
# result --> 5, 7, 2
