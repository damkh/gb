user_data_as_dict = {
    'first_name': 'Иван',
    'last_name': 'Иванов',
    'age': 29,
    'friends': ['Вася', 'Дима'],
}

# for el in user_data_as_dict:
#     print(el)
#
# for el in user_data_as_dict.keys():
#     print(el)

# for el in user_data_as_dict.values():
#     print(el)

for key, val in user_data_as_dict.items():
    print(f'{key}: {val}')
