Write a Python program that:

○ Asks the user a scale factor a and a common ratio r;

○ Your program inform the user if the GP informed converges to a sum regardless of its number of elements:

■ If the GP converges to a sum regardless of the number of elements, your program should compute the sum of infinite elements;

■ Otherwise, your program should ask the number of elements n, and compute the sum of all elements;

○ With that information, your program should print out the first 3 elements of the GP and the computed sum.

For example, if the user enters: a = 10 and r = 0.5, your program should output:

This GP converges with infinite elements to 20

For example, if the user enters: a = 10 and r = -0.5, your program should output:

This GP converges with infinite elements to 6.6666667

For example, if the user enters: a = 1 and r = 2, your program should output:

This GP does not converge to a finite number with infinite elements and ask for n, and if the user enters n = 10, the final output should be:

This GP sum with 10 elements is equal to 1023