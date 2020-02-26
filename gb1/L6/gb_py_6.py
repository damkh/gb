def f_1():
    f1 = open('a.txt', 'w')
    f2 = open('a.txt', 'r')


def f_2():
    f1 = open('a.txt', 'w')
    f1.write('a1\n')
    f1.write('a2')
    f1.writelines(['\na3\t', 'a4'])


def f_3():
    f1 = open('a.txt', 'r')
    #print(f1.read())

    #for l in f1:
    #    print(l.replace('\n', ''))

    print(f1.readline(10))
    print(f1.readlines())


def f_4():
    f1 = open('a.txt', 'r')
    print(f1.readline(10))
    f1.close()
    #print(f1.readlines())

    with open('a.txt', 'r') as f1:
        for line in f1:
            print(line.replace('\n', ''))


def f_5():
    ss = 'a1'
    sb = b'a2'
    sb1 = b'a2'
    print(type(sb))
    print(sb)

    print('---')
    print(ss[0])
    print(sb[0])

    print('---')
    print(sb[0:1])

    print('---')
    for i in sb:
        print(i)
    print('---')
    for i in sb:
        print(i)


def f_6():
    sb = b'Ad'
    print(sb[0])
    print(sb[1])

def f_7():
    s = 'Hello'
    sb = s.encode('ascii')
    print(sb)
    print(type(sb))

    s1 = 'Hello бла бла бла'
    sb1 = s1.encode('utf-8')
    print(sb1)
    print(type(sb1))

    print(sb1.decode('utf-8'))
    print(type(sb1.decode('utf-8')))


def f_8():
    with open('a.txt', 'wb') as f1:
        f1.write(b'Hello')
    #with open('a.txt', 'r', encoding='ascii') as f1:
    #    print(f1.read())

    with open('b.txt', 'w', encoding='utf-8') as f2:
        f2.write('Привет')
    #with open('b.txt', 'r', encoding='utf-8') as f2:
    #    print(f2.read())
        #pass

    with open('a.txt', 'rb') as f1:
        result = f1.read()
        print(result)
        print(type(result))

    with open('b.txt', 'rb') as f2:
        result = f2.read()
        print(result)
        print(type(result))
        print(result.decode('utf-8'))

    with open('a.txt', 'r', encoding='utf-8') as f1:
        pass


def f_9():
    person = {'name': 'Max', 'phones': [123, 456]}

    with open('a.dat', 'wb') as f:
        name = person['name']
        f.write('{}\n'.format(name).encode('utf-8'))
        phones = person['phones']
        for phone in phones:
            f.write('{}\n'.format(phone).encode('utf-8'))
    print('end')

# pickle
def f_10():
    import pickle
    person = {'name': 'Max', 'phones': [123, 456]}
    with open('a.dat', 'wb') as f:
        pickle.dump(person, f)

    with open('a.dat', 'rb') as f:
        print(pickle.load(f))

    print('end')


def f_11():
    import json
    friends = [
        {'name': 'Max', 'phones': [123, 456], 'age': 22},
        {'name': 'Leo', 'phones': [789, 000]}
    ]
    print(type(friends))

    json_friends = json.dumps(friends)
    print(type(json_friends))
    print(json_friends)

    friends1 = json.loads(json_friends)
    print(friends1)
    print(type(friends1))

    x = '232'
    j_x = json.dumps(x)
    print(j_x)
    print(type(j_x))


def f_12():
    import json
    friends = [
        {'name': 'Max', 'phones': [123, 456], 'age': 22},
        {'name': 'Leo', 'phones': [789, 000]}
    ]

    with open('a.json', 'w') as f:
        json.dump(friends, f)

    with open('a.json', 'r') as f:
        x = json.load(f)
        print(x)
        print(type(x))


def f_13():
    import json
    tracks = [
        {'name': 'Max', 'artist': 'AAA'},
        {'name': 'Leo', 'artist': 'ЖЖЖ'},
        {'name': 'Петя', 'artist': 'CCC'}
    ]

    with open('tracks.json', 'w', encoding='utf-8') as f:
        json.dump(tracks, f)

def f_hw_1():
    import json, pickle
    my_favourite_group = {
        'name': 'Г.М.О.',
        'tracks': ['Последний месяц осени', 'Шапито'],
        'Albums': [
            {'name': 'Делать панк - рок', 'year': 2016},
            {'name': 'Шапито', 'year': 2014}
            ]
    }

    my_pickle = pickle.dumps(my_favourite_group)
    print(my_pickle)
    my_json = json.dumps(my_favourite_group)
    print(my_json)

    with open('hw_1.pickle', 'wb') as f_pickle:
        pickle.dump(my_favourite_group, f_pickle)

    with open('hw_1.json', 'w', encoding='utf-8') as f_json:
        json.dump(my_favourite_group, f_json)


def f_hw_2():
    import json, pickle
    with open('hw_1.pickle', 'rb') as f:
        my_pickle = pickle.load(f)
        print(my_pickle)
        print(type(my_pickle))

    with open('hw_1.json', 'r', encoding='windows-1251') as f:
        my_json = json.load(f)
        print(my_json)
        print(type(my_json))


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
#f_hw_1()
f_hw_2()