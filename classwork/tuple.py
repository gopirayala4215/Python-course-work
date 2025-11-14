t = ()
print(t)

t = tuple()
print(t)

t = (1, 2, 3, 4, 5, 1, 2, 4)
print(t)

t = tuple((1, 2, 3, 4, 5))
print(t)

t = 1, 2, 3, 4, 5
print(t)

t = (1,)
print(t)

t = ('int','float','complex','bool','set','dict','list','tuple','string')
print(t)

print(t[1])
print(t[-1])
print(t[-2])
print(t[-5])
print(t[2])
print(t[3])

print(t[3:6])
print(t[-1:-4])
print(t[-1:-4:-1])
print(t[-3:])
print(t[2::-1])
print(t[::2])
print(t[::-2])

t1 = (1, 2, 3)
t2 = (7, 8, 9)
print(t1 + t2)
print(t1 * 5)

print(3 in t1)
print(5 in t1)
print(4 not in t1)
print(1 not in t1)

t = (10, 20, 30)
a, b, c = t
print(a, b, c)

t = ('Uname', 'mail@gmail.com', 'Pwd@123')
uname, mail, pwd = t
print(uname, mail, pwd)

t = (1, 2, 3, 1, 2, 3, 1, 2)
print(t.count(2))
print(t.count(3))
print(t.count(1))
print(t.index(2))

print(len(t))
print(max(t))
print(min(t))
print(sum(t))

