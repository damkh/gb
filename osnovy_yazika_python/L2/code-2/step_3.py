import copy

a = [15, 147.5, 'hello', True, 15]
b = copy.copy(a)

print(id(a), id(b))
b[0] = 'jump'
print(a)
print(b)

