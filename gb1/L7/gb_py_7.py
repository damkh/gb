def f_1():
    has_name = False
    name = 'Max' if has_name else 'Empty'
    print(name)

    is_one = True
    number = 1 if is_one else 2
    print(number)

    is_russian = False
    print('Привет' if is_russian else 'Hello')


def f_2():
    word = 'someworduHYddJNJNdqwj'

    result=[]

    for i in range(len(word)):
        #if i % 2 != 0:
        #    letter = word[i].lower()
        #else:
        #    letter = word[i].upper()
        letter = word[i].lower() if i % 2 != 0 else word[i].upper()
        result.append(letter)

    result = ''.join(result)
    print(result)


def f_3():
    password = input('Enter password: ')

    print('Access accept' if password == 'secret' else 'Access denied!')


def f_4():
    numbers = [1, 9, -4, 2, -5, -9, 2, 7]

    # 1
    result = []
    for number in numbers:
        if number > 0:
            result.append(number)

    print(numbers)
    print(result)

    # 2
    print(list(filter(lambda number: number > 0, numbers)))

    # 3
    result = [number for number in numbers if number > 0]
    print(result)


def f_5():
    pairs = [(1, 'a'), (2, 'b'), (3, 'c'), ('qq', 'qq'), ('7', 'c')]
    # 1
    result = {}
    for i in pairs:
        if isinstance(i[0], int):
            result[i[0]] = i[1]
    print(result)

    # 2
    result = {i[0]: i[1] for i in pairs if isinstance(i[0], int)}
    print(result)

def f_6():
    import random
    result = [random.randint(1, 100) for i in range(1, 10)]
    print(result)
    result1 = [i**2 for i in result]
    print(result1)
    names = ['Alice', 'Max', 'Leo', 'archi', 'Kate', 'Andrew']
    result2 = [name for name in names if (name[0] == 'A' or name[0] == 'a')]
    result3 = [name for name in names if name[0] == 'A']
    print(result2)
    print(result3)


def f_7():
    s = ''
    print('Not empty' if s else 'Empty')

    l = [1, 2, 4]
    d = {1: 2, 3: 4}
    print('Not empty' if l else 'Empty')
    print('Not empty' if d else 'Empty')


def f_8():
    import math

    if 1 > 2 and math.sqrt(-1):
        print('Nothing')

    #if math.sqrt(-1) and 3 > 2:
    #    print('Nothing')

    print('a' and '1' and '0' and None)
    print((bool('a') and bool('1')) and bool(None))

    if 3 > 2 or math.sqrt(-1):
        print('Nothing')


def f_9():
    import math

    numbers = [1, 9, -4, 2, -5, -9, 3, 7]
    print(numbers)
    result1 = []
    for number in numbers:
        if number > 0:
            if math.sqrt(number) < 2:
                result1.append(round(math.sqrt(number), 2))
    print(result1)

    result2 = []
    for number in numbers:
        if number > 0 and math.sqrt(number) < 2:
            result2.append(round(math.sqrt(number), 2))
    print(result2)

    result3 = [round(math.sqrt(number), 2) for number in numbers if number > 0 and math.sqrt(number) < 2]
    print(result3)

def f_10():
    def add_to_list(input_list=None):
        if input_list is None:
            input_list = []
        input_list.append(2)
        return input_list

    print(add_to_list())
    print(add_to_list([0, 1]))

    def add_to_list_1(input_list=None):
        input_list = input_list or []
        input_list.append(2)
        return input_list

    print(add_to_list_1())
    print(add_to_list_1([0, 1]))

def f_11():
    a = 1
    b = a
    b = 100
    print(a, b)

    a = [1, 2, 3]
    b = a
    b[2] = 100
    print(b)
    print(a)

def f_12():
    numbers = [1, 2, 3]
    def change_number_in_list(input_list):
        input_list[1] = 200

    print(numbers)
    change_number_in_list(numbers)
    print(numbers)


def f_13():
    import copy

    numbers = [1, 2, 3]
    numbers_1 = numbers[:]
    numbers_2 = numbers
    numbers_3 = numbers.copy()
    numbers_1[1] = 150
    numbers_2[1] = 180
    numbers_3[1] = 170

    print(numbers)
    print(numbers_1)
    print(numbers_2)
    print(numbers_3)

    a = [1, 2, [3, 4]]
    b = a[:]
    b[2][1] = 100
    print(a)
    print(b)

    c = copy.deepcopy(a)
    c[2][1] = 150
    print(a)
    print(c)

    #change_number_in_list(numbers)
    #print(numbers)

def f_14():
    import math
    number = int(input('Enter your number: '))
    try:
        print(100 / math.sqrt(number))
    except ZeroDivisionError as e:
        print('Error', e)
    except Exception as e:
        print('Call admin')
        print('Error', e)


def f_15():
    import math
    number = int(input('Enter number: '))
    try:
        x = 100 / math.sqrt(number)
    except ZeroDivisionError as e:
        print('/0')
    except:
        print('Call admin')
    else:
        print(f'Result of {number}/100 is:', x)
    finally:
        print('calculation completed')


def f_16():
    a = int(input('Enter number not 5: '))
    if a == 5:
        raise ValueError('number = 5')
    else:
        print(f'{a} != 5')
    print('End')

#f_1()
#f_2()
#f_3()
#f_4()
#f_5()
#f_6()
#f_7()
#f_8()
#f_9()
#f_10()
#f_11()
#f_12()
#f_13()
#f_14()
#f_15()
f_16()