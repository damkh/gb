user_data = 'Иван Иванов 25 199 99'

first_name, last_name, age, *others = user_data.split()

print(first_name, last_name, age)
print(others)

a, b, c = 15, 'go', True
print(a, b, c)

a, b, c = b, c, a
print(a, b, c)
