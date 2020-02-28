a = [15, 147.5, 'hello', True, 15]
# b = a[:]  # shallow copy, deepcopy
# b = list(a)
b = a.copy()

print(id(a), id(b))
b[0] = 'jump'
print(a)
print(b)

