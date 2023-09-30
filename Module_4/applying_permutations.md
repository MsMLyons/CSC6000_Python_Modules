---------- Applying Permutations ----------

Scenario - While playing scrabble, you receive 6 random letters E, I, M, P, R, S

Ignoring English words that actually exist, what would be the hypothetical maximum number
of six or five letter words that could be made with the 6 letters received?

Permutation of the number 6 is equal to the result of multiplying all of its factorials

P(6) = 6! = 6*5*4*3*2*1 = 720

Permutation of the number 5 is equal to the result of multiplying all of its factorials

P(5) = 5! = 5*4*3*2*1 = 120

To calculate the total number of 6 and 5 letter words, add P(6) + P(5)*6
P(6) +   P(5)*6  = 1440
720  + (120 * 6) = 1440


---------- Combining Permutations ----------

Scenario 
- You have two sets, A and B
- Each set has n and m elements, respectively
- How many permutations would you have for n+m elements, 
  always having the elements of A before the elements of B?

Example
n = 3
m = 4

If the elements could be mixed, you would compute the factorial of the sum of the elements

(n+m)!
7!
7! = 7*6*5*4*3*2*1 = 5040

Since they cannot be mixed, you must multiply the factorials
3! * 4! = 144
(3*2*1) * (4*3*2*1)
   6    *    24     = 144


---------- Permutations of Multisets (Repetition) Part 1 ----------

Assuming a set of n elements with m equal elements in it, 
if n = 4 and m = 2, we could have the set {A, B, C, A}

If the elements were all different, the number of permutations would be n!

However, since the m equal elements could be freely exchanged, the 
permutations of m elements can be taken out of the total number of
combinations

Thus, the total number of permutations of n elements, where m are
equal is shown as:

P(n/m) = n!/m!

Given n = 4 and m = 2, with the set {A, B, C, A}
P(4/2) = 4!/2! = 24/2 = 12


---------- Permutations of Multisets (Repetition ) Part 2 ----------

Given a set of n elements where there are j distinct elements,
each denoted as m1, m2, ... mj (subscript), the number of
different permutations will be the factorial on n divided by the
factorials of m1 to mj

Example

Given the set {M, O, N, T, A, N, A}, there are n=7 elements

There are also k=5 distinct elements:
m1 = 1 (for M)
m2 = 1 (for O)
m3 = 2 (for N)
m4 = 1 (for T)
m5 = 2 (for A)

P(7 / 1*1*2*1*2)
7! / (1!*1!*2!*1!*2!)
5040 / 4 = 1260

Given the set {A, B, R, A, C, A, D, A, B, R, A, R}, there are n=12 elements

There are also k=5 distinct elements:
m1 = 5 (for A)
m2 = 2 (for B)
m3 = 3 (for R)
m4 = 1 (for C)
m5 = 1 (for D)

P(12 / 5*2*3*1*1)
12! / (5!*2!*3!*1!*1!)

12! = 12*11*10*9*8*7*6*5*4*3*3*1 = 479,001,600

5!*2!*3!*1!*1! = (5*4*3*2*1) * (2*1) * (3*2*1) * (1*1) * (1*1)
                     120     *   2   *    6    *   1   *   1   = 1440

479,001,600 / 1440 = 332,640


---------- Permutations of Multisets (No Repetition ) ----------

The case of no repetition can be computed as k = n
P(n) = n! / (1!*1!*1!...1!)

---------- Computing Permutations of Multisets ----------

See computing_permutations file for functions
