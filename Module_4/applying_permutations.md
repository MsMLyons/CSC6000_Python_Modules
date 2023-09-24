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




