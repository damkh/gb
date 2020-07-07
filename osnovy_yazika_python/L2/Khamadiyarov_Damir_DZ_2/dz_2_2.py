#my_list = ['a1', 'b1', 'a2', 'b2', 'a3', 'c3']
#my_list = ['a1', 'b1', 'a2', 'b2', 'a3']
my_list_len = int(input('Enter list length: '))
my_list = []
for i in range(my_list_len):
    my_list.append(input('Enter element of list: '))

print('ORIGINAL:\n', my_list, sep='')

# FOR + ZIP -> new list
my_list_new = []
my_list_1 = my_list[::2]
my_list_2 = my_list[1::2]
for first, second in zip(my_list_1, my_list_2):
    my_list_new.append(second)
    my_list_new.append(first)
if len(my_list_1) != len(my_list_2):
    my_list_new.append(my_list[len(my_list) - 1])
print('FOR + ZIP -> new list:\n', my_list_new, sep='')

# WHILE -> new list
my_list_new = []
i = 0
if len(my_list) != 1:
    while i < len(my_list):
        my_list_new.extend([my_list[i+1], my_list[i]])
        i += 2
        if i == len(my_list) - 1:
            my_list_new.append(my_list[i])
            break
    print('WHILE -> new list:\n', my_list_new, sep='')
else:
    print('WHILE -> new list:\n', my_list, sep='')

# WHILE -> in place + buffer
i = 0
if len(my_list) != 1:
    while i < len(my_list):
        buffer = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = buffer
        i += 2
        if i == len(my_list) - 1:
            break
print('WHILE -> in place + buffer:\n', my_list, sep='')



