l = []
l = list()
l = [1, 2, 3, 4, 5, 6]
l = list([1, 2, 3, 4, 5])
l = [[1, 2], [3, 4], [5, 6]]
l = [1, 1, 1, 1, 1, 1, 2]
print([1, 2, 3] + [4, 5, 6])
print([1, 2] * 5)
print(2 in l)
print(6 in l)

l = ['ajay', 'krishna', 'shekar', 'santhosh', 'harsha', 'varun', 'shiva']
print(l)
print(l[2])
print(l[-3])
print(l[-2])
print(l[-1])
print(l[1])
print(l[0])
print(l[1:3])
print(l[-1:-4:-1])
print(l[::2])
print(l[1::2])
print(l[::-1])

l = [[1, 2], [3, 4], [5, 6]]
print(l[2])
print(l[1])
print(l[0])
print(l[0][0])
print(l[2][0])
print(l[1][1])

l = [10, 20, 30, 40, 50]
print(id(l))
print(l[1])
l[1] = 20.3
print(l)
print(id(l))
l[2] = 30 + 4j
print(l)
l[3] = 'string'
print(l)

l.append([1, 2, 3])
print(l)
l.append((10, 202, 30))
print(l)
l.append(70)
l.append(80)
print(l)
l.extend([100, 90, 20, 10])
print(l)
l.insert(0, 10)
print(l)
l.insert(5, {1: 2, 2: 4, 3: 6, 4: 8})
print(l)
l.insert(8, {1, 2, 3, 4})
print(l)

l.remove(10)
print(l)
l.remove((10, 202, 30))
print(l)
l.remove({1, 2, 3, 4})
print(l)
l.remove(100)
print(l)

l.pop(2)
print(l)
l.pop(1)
print(l)
l.pop(1)
print(l)
l.pop(1)
print(l)
l.pop()
print(l)
l.pop()
l.pop()
l.pop()
print(l)
del l[2]
print(l)
l.clear()
print(l)

l = [1, 2, 3, 4]
del l

l = [1, 2, 3, 4]
l.clear()
print(l)

l = [10, 20, 30, 40, 50, 60, 70, 80]
print(l.index(30))
print(l.index(80))
l.append(10)
print(l)
print(l.index(10))
print(l.count(10))
l.sort()
print(l)

l = [8, 2, 3, 4, 1, 8, 3, 4]
print(sorted(l))
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)

a = [1, 2, 3, 4, 5]
b = a
b.append(6)
print(a)
print(b)

c = a.copy()
c.append(9)
print(c)
print(a)

l = [1, 2, 3, 3, 4, 4, 8, 8]
print(max(l))
print(min(l))
print(len(l))

l = [0, 0.0, '', [], (), {}, set(), False]
print(any(l))
print(all(l))
l.append(1)
print(l)
print(any(l))
print(all(l))

a = [1, 2, 3, 4, 5, 6]
print(all(a))
