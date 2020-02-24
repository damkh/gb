def f_1():
    import math
    r = 100
    print(2*math.pi*r)
    print(math.pow(r, 2))

    x1 = 10
    y1 = 10
    x2 = 50
    y2 = 100
    print(math.sqrt(math.pow(y2 - y1, 2) + math.pow(x2 - x1, 2)))

    print(math.factorial(5))


def f_2():
    import random
    for i in range(1, 2):
        print(random.randint(0, 10))

    a = ['a1', 'a2', 'a3', 'a4', 'a5']
    print(random.choice(a))
    print(random.sample(a, 3))
    random.shuffle(a)
    print(a)


def f_3():
    from gb.L5.mod_b import f_b, b
    from gb.L5.dir5.mod_a import f_a, a

    f_b()
    print(f_a())
    print(a, b)


def f_4():
    from gb.L5.pkg_5 import get_main
    from gb.L5.pkg_5 import get_10
    get_main()
    get_10()


def f_5():
    import os

    print(os.name)
    print(os.getcwd())

    new_path = os.path.join(os.getcwd(), 'ff')
    #os.mkdir(new_path)
    os.rmdir('ff')


def f_6():
    import sys

    print(sys.executable)
    print(sys.platform)
    #sys.exit()
    print('aaa')


def f_7():
    import sys

    print(sys.path)
    print(type(sys.path))

    for i in sys.path:
        print(i)


def f_8():
    import os, sys

    for i in range(1, 6):
        new_path = os.path.join(os.getcwd(), '{}__{}'.format(sys.platform, i))
        os.mkdir(new_path)


def f_9():
    import sys

    print(sys.argv[0])

    for arg in sys.argv:
        print(arg)
        print(type(arg))


def f_10():
    import sys, os

    def ping():
        print('pong')

    def hello(name):
        print('Hello', name)

    def get_info():
        print(os.listdir())

    command = sys.argv[1]

    if command == 'ping':
        ping()
    elif command == 'list':
        get_info()
    elif command == 'name':
        name = sys.argv[2]
        hello(name)

    #ping()
    #hello('aaa')
    #get_info()


def f_hw_1():
    import os

    def mk_dir():
        for i in range(1, 10):
            print(i)
            os.mkdir(os.path.join(os.getcwd(), '{}_{}'.format('dir', i)))

    def rem_dir():
        for i in range(1, 10):
            print(i)
            os.rmdir(os.path.join(os.getcwd(), '{}_{}'.format('dir', i)))

    mk_dir()
    rem_dir()


def f_hw_2():
    import random
    def rand_elem(list):
        random.seed()
        #return list[random.randint(0, len(list) - 1)]
        if list != []:
            return random.choice(list)
        else:
            return None

    #my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    my_list = []
    #print(len(my_list))
    #print(random(len(my_list)))
    print(rand_elem(my_list))






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
#f_hw_1()
f_hw_2()
