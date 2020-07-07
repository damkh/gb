# user_age = int(input('введите возраст пользователя: '))
user_age = int('12')

if user_age >= 21:
    print('полный доступ к системе')
elif user_age >= 18:
    print('продвинутый доступ к системе')
elif user_age >= 16:
    print('базовый доступ к системе')
else:
    print('доступа к системе нет')
    if user_age >= 14:
        print('но паспорт есть')

print('добро пожаловать')
