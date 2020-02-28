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

# print(user_data_as_dict['weight'])
print(user_data_as_dict.get('weight'))
print(user_data_as_dict.get('weight', 65))
print(user_data_as_dict)
print(user_data_as_dict.setdefault('weight', 65))
print(user_data_as_dict)
print(user_data_as_dict.setdefault('weight', 75))
print(user_data_as_dict)

