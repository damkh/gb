import sys

a = [15, 147.5, 'hello', True, 15]
b = 15, 147.5, 'hello', True, 15

print(type(a), type(b))
print(sys.getsizeof(a), sys.getsizeof(b))

# # mutable
# a[0] = 'go'
# print(a)
# # # immutable
# # b[0] = 'go'
# # print(b)
#
# print(b[0])
