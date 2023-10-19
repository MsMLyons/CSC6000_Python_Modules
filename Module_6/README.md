Write a python program that receives two matrices
The program should verify if the two matrices are the inverse of each other
- to check, try multiplying the matrices
    - if the matrices cannot be multiplied, then they are not inverses of each other
    - if the multiplication does not give an identity matrix, they are not inverses of each other

Step one:
A = matrix 1
B = matrix 2
C = matrix 1 * matrix 2 (if possible)

Step 2:
Create a function to verify if 2 matrices are the inverse of each other
Use the multiplication function
- Test output with a matrix calculator - https://matrix.reshish.com/inverse.php
Each matrix can have up to 10 columns and rows (but no need to write a check for this)
Check for identity matrix?

Multiply A * B --> multAB = A * B
Multiply B * A --> multBA = B * A
Check if multAB == multBA? 

Step 3:
If the matrices are the inverse of each other, print "The matrices are the inverse of each other"
If the matrices are not the inverse of each other, print "The matrices are not the inverse of each other"