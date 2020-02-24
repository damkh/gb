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
    word = 'someword'

    result=[]

    for i in len(word):
        if i % 2:
            letter = word[i].lower()


#f_1()
f_2()