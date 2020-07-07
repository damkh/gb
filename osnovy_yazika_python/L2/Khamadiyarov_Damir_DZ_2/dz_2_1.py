my_list = [1, 2.2, -3, 'string', True, (3 + 2j), ['a', 'b', 4, 3.3], ('c', 'd', 7, 8.8), {'set', 1, 5.5, 5.5},
           {'a1': 'b1', 'a2': 'b2'}]

for el in my_list:
    if type(el) == int:
        print(f'{el}\033[1m - is integer\033[0m')
    else:
        print(f'{el} : {type(el)}\033[1m - is NOT integer\033[0m')
