"dog" + "cat"*2
#reproduce the string "cat" twice & conCATenate lol
"catcat"
#concatenate strings
"dog" + "catcat" = "dogcatcat"

"dog"*2 + "cat"
"dogdog" + "cat"
"dogdogcat"

d = "dog"
d[1]
#pull out the item found at variable d, index 1
"o"

d= "dog"
d[-1]
#pull out the item found at the last index position
"g"

s = "abcdefghijkl"
s[3:]
#slice / pull out the letters in the string starting with index position 3
#and going to the end of the string
"defghijkl"

s = "abcdefghijkl"
s[:-4]
#slice / pull out the letters in the string starting with the beginning 
#of the string and going to index position -4, fourth letter from last
"abcdefgh"

s = "abcdefghijkl"
# s[start:stop:step]
s[2:8:2]
#slice / pull out letters in the string starting with index 2 ("c"), stopping
#at index 8 ("i"), and jumping 2 indices through the sliced string to pull out
#the letters only at every other index, but not including the last one because
#the stopping character is not included in the string
"ceg"


