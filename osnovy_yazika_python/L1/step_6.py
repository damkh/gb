user_age = int('20')

if user_age >= 21:
    print('access grant!')
elif user_age >= 18:
    print('partially access')
else:
    print('access denied')