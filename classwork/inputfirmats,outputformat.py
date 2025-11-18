name = input("Enter the name: ")
print(name)

age = int(input("Enter the age: "))
print(age)

discount = float(input("Enter the discount: "))
print(discount)

names = input("Enter names: ")
print(names)

names = input("Enter multiple names: ").split()
print(names)

names = list(map(int, input("Enter integers: ").split()))
print(names)

names = list(map(float, input("Enter floats: ").split()))
print(names)

names = tuple(input("Enter names for tuple: ").split())
print(names)

names = tuple(map(int, input("Enter ints for tuple: ").split()))
print(names)

names = tuple(map(float, input("Enter floats for tuple: ").split()))
print(names)

names = set(map(int, input("Enter integers for set: ").split()))
print(names)

names = set(map(float, input("Enter floats for set: ").split()))
print(names)

names = set(input("Enter names for set: ").split())
print(names)

d = eval(input("Enter dictionary/list/string using eval: "))
print(d)

name, email = input("Enter name and email: ").split()
print(name)
print(email)

a, b = list(map(int, input("Enter two integers: ").split()))
print(a, b)

a, b, c = 10, 20, 30
print("a=", a, "b=", b, "c=", c)

print("a=", a, "\nb=", b, "\nc=", c)

print("a=", a, "\tb=", b, "\tc=", c)

print(f'a={a}\nb={b}\nc={c}')
print(f'a={a}\tb={b}\tc={c}')

x = 10
y = 23.4
z = "string"

print('a=%d\nb=%f\nc=%s' % (x, y, z))
print('a=%d\nb=%.2f\nc=%s' % (x, y, z))

print('a={}\tb={}\tc={}'.format(x, y, z))
print('a={2}\tb={1}\tc={0}'.format(x, y, z))

