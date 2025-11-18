a = 10
print(float(a))
print(str(a))
print(complex(a))
print(bool(a))

b = 12.5
print(int(b))
print(float(b))
print(str(b))
print(complex(b))
print(bool(b))

s = 'python'
print(list(s))
print(tuple(s))
print(set(s))

l = [1, 2, 3, 4, 5]
print(str(l))
print(tuple(l))
print(set(l))
print(bool(l))

t = (1, 2, 3, 4, 5)
print(str(t))
print(list(t))
print(set(t))
print(bool(t))

s = {1, 2, 2, 4, 5}
print(s)
print(str(s))
print(list(s))
print(tuple(s))
print(bool(s))

d = [(1,2),(3,4),(5,6),(7,8)]
print(dict(d))

d = {1:1, 2:4, 3:9}
print(list(d))
print(tuple(d))
print(set(d))

string = input("Enter the string: ")
print(string)

i = input("Enter a number: ")
print(i)

i = int(input("Enter integer: "))
print(i)

i = float(input("Enter float: "))
print(i)

i = list(input("Enter characters: "))
print(i)

i = list(input("Enter comma-separated values: ").split(','))
print(i)

l = list(map(int, input("Enter comma-separated integers: ").split(',')))
print(l)

l = list(map(float, input("Enter comma-separated floats: ").split(',')))
print(l)































