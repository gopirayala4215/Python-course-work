# Integer variable
int_a = 10
print(type(int_a))

# Float variable
float_b = 299.5
print(type(float_b))

# Complex number
complex_c = 2 + 7j
print(type(complex_c))

# String variables
str_s = 'codegnan'
print(type(str_s))

s = "batch-41"
print(type(s))

s = '''python programming'''
print(type(s))

a = s
print(a)
print(s)

# id() shows memory location
print(id(s))
s = s + 'lang'
print(s)
print(id(s))

# List operations
l = [1, 2, 3]
l.append(4)
print(id(l))
l.append(7)
print(l)
print(id(l))

l = [1, 2, 3, 4, 5]
print(l)

l = list()
print(l)

l = []
print(l)

print(type(1))

# List of names
names = ['ajay', 'kridhna', 'sathish', 'vishal']
print(names)
names.append('anirudh')
print(names)

# Tuple
t = (12.4567890, 12.567890)
print(t)

# Set
fav = {'laptop', 'bike', 'phone', 'car'}
print(fav)

# Changing fav to a list
fav = [1, 1, 1, 2, 2, 1, 2]
print(fav)
print(fav[1])

fav = [1, 2]
print(fav)

# Tuple creation
t = ()
t = tuple()
print(type(t))

# Assigning string to t
t = s
print(type(s))
print(s)
print(t)

# Set examples
s = set()
print(s)

s = {1, 2, 3, 4, 5}
print(s)

# Frozen set
s = frozenset({1, 2, 3, 4})
print(s)
print(type(s))
