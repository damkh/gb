a = [1, 2, 3, 'h', True, 'h']

for i in range(len(a)):
    print(a[i], a[-i - 1])

for i, j in zip(a, a[::-1]):
    print(i, j)