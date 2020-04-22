 # Operator (=) assigns the value to variable
a = 4; b = 5
print(a, "is of type", type(a))

# Operations
print(a + b)
print(4 + 5)
print(a - a * b)
print(25 - 3 * 6)
print((20 - 3 * 7) / 2)
print(9 / 5)

# division returns a floating point number
c = b / a
print(c, "is of type", type(c))
print(c) # No need to explicitly declare the datatype

a = 4; b = 5   
d = b // a # Floor Division returns an integer
print(d)
print(d, "is of type", type(d))

print(-7 / 5) # Float
print(7 / 5) # Float
print(-7 // 5) # Integer

a = 7; b = 5   
e = b**a # The operator (**) calculates power 
print("power is ", e)
print(a / b)

# Complex Number
f = 3+5j
print(f, "is of type", type(f))
print("real part is", f.real)
print("imaginary part is", f.imag)
print(f * 2) # multiplication
print(f + 3) # addition
print(f - 1) # subtraction

print(bool(2))
print(bool(-2))
print(bool(0))

See_boolean = (4 * 3 > 10) and (6 + 5 >= 11)
print(See_boolean)

if (See_boolean):
  print("Boolean expression returned True")
else:
  print("boolean expression returned False")
