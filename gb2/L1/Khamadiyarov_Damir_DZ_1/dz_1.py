var_int = 1
var_float = 1.1
var_str = '1'
var_bool = True
var_list = [1, True, 'Hi']
var_tuple = (1, True, 'Hi')
var_dict = {
    'one': 1,
    'two': var_bool,
    'three': var_str,
    'four': var_list
}

print(f'var_int = {var_int}')
print('var_float = {}'.format(var_float))
print('type of var_str is %s' % type(var_str))
print('var_list', var_list, sep='SEP')
print(var_tuple)
for i in var_dict:
    print('var_dict(', i, '):', var_dict[i])

#var_input_1 = input('Enter word: ')
#var_input_2 = int(input('Enter number: '))
var_input_1 = '123'
var_input_2 = int('123')
print(f'var_input_1 = {var_input_1}, type is: {type(var_input_1)}')
print(f'var_input_2 = {var_input_2}, type is: {type(var_input_2)}')
