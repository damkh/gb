a = [15, 147.5, 'hello', True, 15]

# idx = 0
# while idx < len(a):
#     print(a[idx])
#     idx += 1

# next(a)

# b = []
# for item in a:
#     print(item)
#     b.append(f'new {item}')
#
# print(b)

for num, item in enumerate(a):
    print(num, item)
#
# # for item in a:
# #     print(a.index(item), item)
# idx = 0
# for item in a:
#     print(idx, item)
#     idx += 1

for idx in range(len(a)):
    print(a[idx])
    a[idx] = f'new {a[idx]}'

print(a)
