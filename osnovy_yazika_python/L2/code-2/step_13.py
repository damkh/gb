user_data_as_list = ['Иван', 'Иванов', 29]

# immutable
user_data_as_dict = {
    'first_name': 'Иван',
    'last_name': 'Иванов',
    'age': 29,
    0: 'Иван',
    (0, 1): 'Иванов',
}

print(user_data_as_list)
print(user_data_as_dict)

print(user_data_as_list[0])
print(user_data_as_dict['first_name'])
print(user_data_as_dict[0])

