Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
def f():
    pass
f()
SyntaxError: invalid syntax
f()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    f()
NameError: name 'f' is not defined
def f():
    pass

f()
def ping():
    return "Ping!"

ping()
'Ping!'
x = ping()
print(x)
Ping!
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'f', 'ping', 'x']
import math
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'f', 'math', 'ping', 'x']
dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
math.pi
3.141592653589793
def volume(r):
    """Returns the volume of a sphere with radius r"""
    v = (4.0 / 3.0) * math.pi * r**3
    retuen v
    
SyntaxError: invalid syntax
def volume(r):
    """Returns the volume of a sphere with radius r"""
    v = (4.0 / 3.0) * math.pi * r**3
    return v

volume(2)
33.510321638291124
help(volume)
Help on function volume in module __main__:

volume(r)
    Returns the volume of a sphere with radius r

def triangle_area(b, h):
    """Compute the area of a triangle with base and height variables"""
    return 0.5 * b * h

triangle_area(3, 7)
10.5
def calculate_centimeter(feet = 0, inches = 0):
    """Converts a length from feet and inches to centimeters"""
    """This function takes in arguments that have already been assigned values"""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm

calculate_centimeter(feet = 5)
152.4
calculate_centimeter(inches = 70)
177.8
calculate_centimer(feet = 4, inches = 3)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    calculate_centimer(feet = 4, inches = 3)
NameError: name 'calculate_centimer' is not defined. Did you mean: 'calculate_centimeter'?
calculate_centimeter(feet = 4, inches = 3)
129.54
calculate_centimeter(inches = 7, feet = 3)
109.22
def g(x = 0, y):
    
SyntaxError: non-default argument follows default argument
def g(y, x = 0):
    return x + y
    """Must list keyword (default) arguments last"""

    
def g(y, x = 0):
    return x + y

g(5)
5
g(7, x = 9)
16
