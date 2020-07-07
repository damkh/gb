a = [15, 147.5, 'hello', True, 'world']

# for idx in range(len(a)):
#     print(a[idx], a[-idx - 1])

print(a)
print(a[::-1])
for first, last in zip(a, a[::-1]):
    print(first, last)


