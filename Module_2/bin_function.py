print("__________INTRO TO BINARY NUMBERS__________")

a = 0b10
b = 0b1100
c = 0B101

print("This should be two:", a)
print("This should be twelve:", b)
print("This should be five:", c)
print("This should be twenty-four:", a * b)
print("This should be seven:", a + c)
print("This should be fifty:", c * 10)

print("__________BIN FUNCTION__________")

twoInBinary = bin(2)
twelveInBinary = bin(12)
fiveInBinary = bin(5)

print("__________PRINTING BINARY LITERALS WITH PREAMBLE__________")
print("This should be two in binary with preambule:", twoInBinary)
print("This should be twelve in binary with preambule:", twelveInBinary)
print("This should be five in binary with preambule:", fiveInBinary)

print("__________BINARY SLICE - REMOVE THE PREAMBLE__________")
print("This should be two in binary:", twoInBinary[2:])
print("This should be twelve in binary:", twelveInBinary[2:])
print("This should be five in binary:", fiveInBinary[2:])
      

