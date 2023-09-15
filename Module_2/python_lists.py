a = [0, 11, 22, 33, 44, 55, 66]

s = ["first", "second", "third"]

b = ["John", 40, "Paul", 42, "George", 43, "Ringo", 40]

c = [77, 88, 99]

#d = a[1:] + c + a[0]

#print(d)
# expected result --> [11, 22, 33, 44, 55, 66, 77, 88, 99, 0]
# result --> TypeError: can only concatenate list (not "int") to list

print(a[1])
# result --> 11

print(a[-1])
# result --> 66

print(s[:2])
# result --> ['first', 'second']

print(s[-2])
# result --> second

print(s[-2:])
# result --> ['second', 'third']

print(s[1:], s[-2])
# result --> ['second', 'third'] second

#print(s[1:].s[-2])
# result --> AttributeError: 'list' object has no attribute 's'

new_s = s[1:] and s[-2]
print(new_s)
# result --> second

new_S = [s[1:], s[-2]]
print(new_S)
# result --> [['second', 'third'], 'second']

New_s = new_s = s[1:] and s[-2:]
print(New_s)
# result --> ['second', 'third']

New_S = [s[1:], s[-2:]]
print(New_S)
# result --> [['second', 'third'], ['second', 'third']]

print(s[1:], s[-2:])
# result --> ['second', 'third'] ['second', 'third']

s.append("fourth")
print(s)
# result --> ['first', 'second', 'third', 'fourth']

#b.insert(2, "Yoko").insert(3, 33)
#print(b)
# result --> AttributeError: 'NoneType' object has no attribute 'insert'

print(b[0:-1:2])
#result --> ['John', 'Paul', 'George', 'Ringo']

b.insert(2, "Yoko")
print(b)
# result --> ['John', 40, 'Yoko', 'Paul', 42, 'George', 43, 'Ringo', 40]
# observation: "Yoko" added at index 2

b.insert(3, 33)
print(b)
# result --> ['John', 40, 'Yoko', 33, 'Paul', 42, 'George', 43, 'Ringo', 40]
# observation: 33 added at index 3

print(b[0:-1:2])
# result --> ['John', 'Yoko', 'Paul', 'George', 'Ringo']

#b.pop(0)
#print(b)
# result --> [40, 'Yoko', 33, 'Paul', 42, 'George', 43, 'Ringo', 40]

#b.pop(0)
#print(b)
# result --> ['Yoko', 33, 'Paul', 42, 'George', 43, 'Ringo', 40]

b.pop(0)
b.pop(0)
print(b)
# result --> ['Yoko', 33, 'Paul', 42, 'George', 43, 'Ringo', 40]

#b.pop(0, 1)
#print(b)
# result --> TypeError: pop expected at most 1 argument, got 2
# observation --> can only use pop to remove one list element at a time

b.remove("George")
b.remove(43)
print(b)
# result --> ['Yoko', 33, 'Paul', 42, 'Ringo', 40]

s.reverse()
print(s)
# result --> ['fourth', 'third', 'second', 'first']

s.sort()
print(s)
# result --> ['first', 'fourth', 'second', 'third']
# observation --> alphabetical order

#print(s.len())
# result --> AttributeError: 'list' object has no attribute 'len'

s.copy()
print(s)
# result --> returns a copy of the list ['first', 'fourth', 'second', 'third']

x = s.index("second")
print(x)
# result --> 2

y = ["two", "two", "two", "porcupine", "pineapple", "pickle", "two"]
z = y.count("two")
print(z)
# result --> 4

pine_apple = y.index("pineapple")
print(pine_apple)
# result --> 4

toys = ["puzzle", "doll", "blocks"]
play_areas = ["outside", "bedroom", "living room"]
toys.extend(play_areas)
print(toys)
# result --> ['puzzle', 'doll', 'blocks', 'outside', 'bedroom', 'living room']

animals = ["horse", "cow", "llama", "cat", "dog", "sheep", "mouse"]
animals.insert(0, "chicken")
print(animals)
# result --> ['chicken', 'horse', 'cow', 'llama', 'cat', 'dog', 'sheep', 'mouse']

animals.clear()
print(animals)
# result --> [] (empty list)

kitchen = ["toaster", "fridge", "instapot", "air fryer", "blender"]
size = len(kitchen)
print(size)
# result --> 5

candles = ["cinnamon bun", "pumpkin spice", "autumn foliage", "apple pie"]
size = 0
for item in candles:
    size +=1
print(size)
# result --> 4

pens = ["blue", "black", "red", "purple", "green", "gel", "sharpie", "roller ball"]
print(len(pens))
# result --> 8


new_list = list(("pickles", "olives", "artichokes"))
print(new_list)
