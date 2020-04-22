# Create an empty tuple
t = tuple()
print("Type of tuple t is ", type(t))

# Create a tuple with 1 element
t = ('a',)
print("Tuple t is", t)
print('Type of t is ', type(t))

tpl = ('a', 'b', 'c')
print("Another tuple tpl:", tpl)
print("Another way to create a tuple", tuple('sequence'))

# Multiple assignment
x, y, z = tpl 
print("Value of element x in tuple is", x)
print("Value of element y in tuple is", y)
print("Value of element z in tuple is", z)

# Membership can be tested
print('a' in tpl)
print('z' in tpl)

# Braces are optional
tupl = 1, 2, 3, 4, 5
print("Tuple value at index 1 is", tupl[1])
print("Tuple[1:3] is ", tupl[1:3])

# Tuple concatenation & repetition
tupl2 = (11, 12, 13)
tupl3 = tupl + tupl2
print("Tuple concatenation", tupl3)
print("Tuple repetition is", tupl * 2)
print("membership test", 5 in tupl)

# Tuple Negative Indexing
print("Tuple negative indexing", tupl[-1])     # negative indexing

# Tuple Functions
print("Length of tuple is ", len(tupl))
print("Maximum value in tuple is", max(tupl))
print("Minimum value in tuple is", min(tupl))

# Comparison
print (tupl == tupl2)
print (tupl > tupl2)
