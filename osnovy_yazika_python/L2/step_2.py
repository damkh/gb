# TODO dir(list)
a1 = [1, 2, 3, 'h', True, 'h']
a2 = [2, 5, 6.5, 33, -5, 3, -2.1]

print(dir(a1))
d = a1.pop()
#print(dir(a))
print(a1.index('h'))
b = sorted(a2)
c = sorted(a1)
print(b, id(b))
print(a2, id(a2))
a2.sort()
print(a2, id(a2))

