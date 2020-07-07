a = 'a b c'
a, b, c = a.split()
print(a, b, c)

a, b = b, a
print(a, b, c)