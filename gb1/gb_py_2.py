def f1():
    a = 'abcdefg hijklm'
    b = 45

    print('_start_' + a + '_middle_' + str(b) + '_end_')
    print('_start_%s_middle_%d_end_' % (a, b))
    print('_start_{}_middle_{}_end_'.format(a, b))


def f_top5():
    top5 = 'First 5 on competition: 1. Ivanov 2. Petrov 3. Sidorov 4. Orlov 5. Sokolov'
    start = top5.find('1.')
    end = top5.find('4.')
    print('Congrat {} with the success'.format(top5.upper()[start:end - 1]))


def f_list():
    a3 = 'qq'
    a = ['a1', 'a2', a3]
    print('all: {}'.format(a))
    print('1: {}, 2: {}, 3: {}'.format(a[0], a[1], a[2]))
    print('1 -> 3: {}'.format(a[0:3]))
    print(len(a))
    a.append('rr')
    print(len(a))
    print('all: {}'.format(a))
    print(a.pop())
    print('all: {}'.format(a))
    a.clear()
    print('all: {}'.format(a))
    a = ['b1', 'b2', a3]
    a.remove('b2')
    print('all: {}'.format(a))
    a = ['a1', 'a2', 'b1', 'b2', a3]
    del a[1:3]
    print('all: {}'.format(a))


def f_in():
    a = 'abcdefg'
    if a.find('s') != -1:
        print('is in')
    else:
        print('not in')

    if 'e' in a:
        print('is in')
    else:
        print('not in')

    b = ['abc', 'def', 'ghi']
    if 'def' in b:
        print('is in')
    else:
        print('not in')


def f_competition():
    print('COMPETITION')
    count = int(input('Enter count: '))

    i = count
    members = []
    while i > 0:
        name = input('Who is on {} place?  '.format(i))
        members.append(name)
        print(name)
        i -= 1
    print('all: ', members)
    members.reverse()
    print('all: ', members)
    print('1 -> 3: {} YEEE'.format(members[:3]))
    print(sorted(members))


def f_for():
    a = ['a1', 'a2', 'a3']
    b = ('b1', 'b2', 'b3')

    i = 0
    while i < len(a):
        print('a[{}]: {}'.format(i, a[i]))
        i += 1

    print('all a: ', a)
    for x in a:
        print('a[]: {}'.format(x))

    print('all b: ', b)
    for x in b:
        print('b[]: {}'.format(x))


def f_range():
    a = ['a1', 'a2', 'a3', 'a4', 'a5']
    n = range(10)
    print(n)
    print(type(n))
    print(list(n))

    for i in range(len(a)):
        print('a[{}]: {}'.format(i + 1, a[i]))

    print(list(range(1, 100, 2)))


def f_dict():
    a = ['a1', 'a2', 'a3', 'a4', 'a5']
    b = {
        'n1': 'a1',
        'n2': 'a2',
        'n3': 3
    }
    print(b)
    print(type(b))
    print(b['n2'])
    b['n2'] = 'a22'
    b['n4'] = 'a4'
    print(b)
    del b['n2']
    print(b)

    if 'n2' in b:
        print('is in')
    else:
        print('not in')

    for k in b.keys():
        print(k, ' ', b[k])

    for k in b.values():
        print(k)

    for k in b.items():
        print(type(k), ' ', k)

    for k1, k2 in b.items():
        print(k1, ' ', k2)


def f_set():
    a = ['a1', 'a2', 'a3', 'a1', 'a3']
    b = set(a)
    print(a)
    print(set(a))
    print(type(set(a)))

    b.add('a5')
    print(b)
    b.add('a3')
    print(b)
    b.remove('a3')
    print(b)
    print(len(b))

    for i in b:
        print(i)

    a = {'a1', 'a2', 'a3', 'a5', 'a4'}
    b = {'a1', 'a5', 'a7', 'a4', 'a6'}
    print(a)
    print(b)
    print(a | b)
    print(a & b)
    print(a - b)
    print(a - (a & b))
    print(b - a)


def f_hw_1():
    my_list_1 = [2, 5, 8, 2, 12, 12, 4, 7]
    my_list_2 = [2, 7, 12, 3]

    for i in my_list_2:
        if i in my_list_1:
            print('will removed: ', i)
            while i in my_list_1:
                print('will removed again: ', i)
                my_list_1.remove(i)

    print(my_list_1)


def f_hw_11():
    my_list_1 = [2, 5, 8, 2, 12, 12, 4, 7]
    my_list_2 = [2, 7, 12, 3]

    for i in my_list_1[: ]:
        if i in my_list_2:
            my_list_1.remove(i)

    print(my_list_1)


def f_hw_2():
    date_day = ['первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое',
                'десятое', 'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
                'семнадцатое', 'восемнадцатое', 'девятнадцатое']
    date_day_dec = ['двадцатое', 'тридцатое']
    date_day_dec_1 = ['двадцать', 'тридцать']
    date_month = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
                  'ноября', 'декабря']

    while True:
        date_all = str(input('input date in format dd.mm.yyyy: '))
        if len(date_all.split('.')) == 3:
            if 1 <= int(date_all.split('.')[0]) <= 31 and \
                    1 <= int(date_all.split('.')[1]) <= 12 and \
                    int(date_all.split('.')[2]) >= 1:
                print('date length and format are correct')
                break
            else:
                print('date format is incorrect')
        else:
            print('date length is incorrect')

    print(date_all.split('.'))

    if int(date_all.split('.')[0]) < 20:
        date_day_str = date_day[int(date_all.split('.')[0]) - 1]
    elif int(date_all.split('.')[0]) == 20 or int(date_all.split('.')[0]) == 30:
        date_day_str = date_day_dec[int(date_all.split('.')[0]) // 10 - 2]
    else:
        date_day_str = date_day_dec_1[int(date_all.split('.')[0]) // 10 - 2] + ' ' + \
                       date_day[int(int(date_all.split('.')[0])) % 10 - 1]

    date_month_str = date_month[int(date_all.split('.')[1]) - 1]

    print('Дата', date_all, 'в текстовом формате:', date_day_str, date_month_str, date_all.split('.')[2], 'года')

def f_hw_3():
    my_list_1 = [2, 2, 5, 12, 8, 2, 12]
    #print(len(my_list_1))
    print(my_list_1)
    repeated_item_set = set()

    for i in range(0, len(my_list_1), 1):
        for j in range(i, len(my_list_1), 1):
            #print(i, j)
            if i != j:
                if my_list_1[i] == my_list_1[j]:
                    #print(i, '\'th: is ', my_list_1[i], ' and ',  j, '\'th: is ', my_list_1[j], sep='')
                    repeated_item_set.add(int(my_list_1[i]))
                    break

    print(repeated_item_set)
    my_list_1_set = set(my_list_1)
    result_list = my_list_1_set - repeated_item_set
    print(list(result_list))



# f1()
# f_top5()
# f_list()
# f_in()
# f_competition()
# f_for()
# f_range()
# f_dict()
# f_set()
#f_hw_1()
#f_hw_11()
# f_hw_2()
#f_hw_3()
