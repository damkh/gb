import copy

a1 = [1, 2, 3, 'h', True, 'h']
a2 = a1
print(id(a1), id(a2))
a3 = copy.copy(a1)
a4 = a1.copy()
print(id(a1), id(a2), id(a3), id(a4))