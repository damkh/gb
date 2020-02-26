#first_name = 'Ivan'
first_name = input('Enter your name: ')
user_age = int(input('Enter your age: '))
print('Hello ', first_name, ', you are ', user_age + 0, ' years old!', sep='')
print('Hello %s, you are %d years old!' % (first_name, user_age))
print('Hello {}, you are {} years old!'.format(first_name, user_age))
print(f'Hello {first_name}, you are {user_age} years old!')

