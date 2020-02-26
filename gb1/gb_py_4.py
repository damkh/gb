def f_builtin_func():
    print(-7, abs(-7))

    nums = [5, 2, 7, 3, 99, 6, 2]
    print(min(nums), max(nums))
    print(sum(nums))

    print(round(30.2999999, 2))

    a = ['a1', 'a2', 'a3']
    for i, an in enumerate(a, 1):
        print(i, an)

    nums1 = []

    for i in range(3):
        nums1.append(int(input('Enter element: ')))

    print(min(nums1), max(nums1), sum(nums1))


def f_sep(sep, sep_len):
    return sep * sep_len


# text = 'a {} b {}'.format(f_sep('v', 15), f_sep('x', 5))
# print(text)


def hello(greet='Hello', *args):
    print(greet, args)


def hello_1(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


def f_my1():
    a = 999
    print(a)


def f_my2():
    global glob_1
    print(glob_1)
    glob_1 = 2
    print(glob_1)


def f_b1():
    a = 1
    print(a)

    def f_b2():
        b = 2
        print(a, b)

        def f_b3():
            c = 3
            print(a, b, c)

        f_b3()

    f_b2()


def f_func_obj():
    def some_f():
        return 10

    result = some_f()
    print(result)

    a = some_f
    print(a, type(a))

    print(a())


def f_func_as_arg():
    def f1():
        print('a1 from f1')

    def f2(f_param):
        f_param()

    f2(f1)


def f_func_as_arg_2():
    def my_filter(nums):
        result = []
        for i in nums:
            if i % 2 == 0:
                result.append(i)
        return result

    def my_filter_f(nums, func):
        result = []
        for i in nums:
            if func(i):
                result.append(i)
        return result

    nums = [1, 2, 3, 4, 5, 66, 77, 88, 99]

    def chet(n):
        return n % 2 == 0

    def nechet(n):
        return n % 2 != 0

    def more_than(n):
        return n > 55

    print(my_filter(nums))
    print(my_filter_f(nums, chet))
    print(my_filter_f(nums, nechet))
    print(my_filter_f(nums, more_than))
    print(my_filter_f(nums, lambda n: n > 70))


def builtin_func_in_func():
    numbers = [2, 5, 5, 77, 5, 23, 0, -5]
    print(sorted(numbers))
    print(sorted(numbers, reverse=True))

    names = ['a1', 'a2', 'a3']
    print(sorted(names))
    print(sorted(names, reverse=True))

    cities = [('a4', 10), ('a2', 50), ('a3', 30), ('a5', 15)]
    print(sorted(cities))
    print(sorted(cities, reverse=True))

    def by_count(city):
        return city[1]

    print(sorted(cities, key=lambda city: city[1]))
    # print(sorted(numbers, key=by_count, reverse=True))


def builtin_func_in_func_2():
    nums = (1, 2, 3, 4, 5, 66, 77, 88, 99)

    def chet(n):
        return n % 2 == 0

    print(filter(chet, nums), list(filter(chet, nums)))

    a = ['a1111', 'a22', 'a3']

    print(list(filter(lambda x: len(x) > 2, a)))


def builtin_func_in_func_3():
    numbers = [2, 5, 5, 77, 5, 23, 0, -5]
    print(list(map(lambda x: x ** 2, numbers)))
    print(list(map(lambda x: str(x), numbers)))


def f_hw_1():
    def f(name, age, city):
        result = '{}, {} year(s) old, lives in {}'.format(name, age, city)
        return result

    print(f('vasya', 22, 'moscow'))


def f_hw_2():
    def f(a1, a2, a3):
        return max([a1, a2, a3])

    print(f(2, 5, 77))


def f_hw_3():
    player1 = {
        'name': 'a1',
        'health': 70,
        'damage': 20
    }
    player2 = {
        'name': 'a2',
        'health': 100,
        'damage': 10
    }

    print('PLAYER1', player1)
    print('PLAYER2', player2)
    for p in player1, player2:
        print('Player {} has health {}'.format(p['name'], p['health']))

    def f(p1, p2):
        p2['health'] -= p1['damage']
        return p2

    for i in range(10):
        player2 = f(player1, player2)
        player1 = f(player2, player1)
        for p in player1, player2:
            print('Player {} has health {}'.format(p['name'], p['health']))

    print('PLAYER1', player1)
    print('PLAYER2', player2)


def f_hw_4():
    player1 = {
        'name': 'a1',
        'health': 70,
        'damage': 20,
        'armor': 1.2
    }
    player2 = {
        'name': 'a2',
        'health': 100,
        'damage': 11.5,
        'armor': 1.5
    }

    for p in player1, player2:
        print('Player {} has health {}'.format(p['name'], p['health']))

    def f_armor(d, a):
        return d/a

    def f_attack(p1, p2):
        p2['health'] -= f_armor(p1['damage'], p2['armor'])
        return p2

    for i in range(10):
        player2 = f_attack(player1, player2)
        player1 = f_attack(player2, player1)
        for p in player1, player2:
            print('Player {} has health {}'.format(p['name'], p['health']))


# f_builtin_func()
# f_sep('x', 40)
# hello(who='Hi', greet='Maa')
# hello('Hi')
# hello()
# hello('Hi', 'a1', 'a2')
# hello('Hi', ('a4', 'a3'))
# hello_1(a='a1', b='b1', c='c1', d='a2', e='b2')
# f_my1()
# f_my2()
# f_b1()
# f_func_obj()
# f_func_as_arg()
# f_func_as_arg_2()
# builtin_func_in_func()
# builtin_func_in_func_2()
# builtin_func_in_func_3()
f_hw_1()
