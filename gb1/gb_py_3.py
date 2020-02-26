import random

def f_play():
    n = random.randint(1, 100)
    #print(n)

    user_num = None
    count = 0

    level = int(input('Enter level: '))
    levels = {
        1: 10,
        2: 5,
        3: 3
    }
    max_count = levels[level]

    user_count = int(input('How many users are playing: '))
    users = []
    for i in range(user_count):
        user_name = input('Enter user {}: '.format(i+1))
        users.append(user_name)

    print(users)

    is_winner = False
    winner_name = None

    while not is_winner:
        count += 1
        if count > max_count:
            print('No attempts more, All users - LOSER!')
            break
        print('Attempt number: {}'.format(count))
        for user in users:
            print('Attempt of {}: '.format(user))
            user_num = int(input('Enter number: '))
            if n == user_num:
                is_winner = True
                winner_name = user
                break
            if n < user_num:
                print('Your num MORE, please decrease')
            elif n > user_num:
                print('Your num LESS, please increase')
    else:
        print('{} WINNER!'.format(winner_name))


def f_hw():
    upper_limit = int(input('Enter upper limit: '))
    lower_limit = int(input('Enter lower limit: '))
    comp_num = (upper_limit - lower_limit + 1) // 2
    flag = None
    attempt_count = 0
    while flag != '=':
        attempt_count += 1
        print('Attempt #: {}, computer said: {}'.format(attempt_count, comp_num))
        flag = input('Enter your answer like "My number is >, < or =": ')
        if flag == '>':
            lower_limit = comp_num
            comp_num += (upper_limit - lower_limit + 1) // 2
        elif flag == '<':
            upper_limit = comp_num
            comp_num -= (upper_limit - lower_limit + 1) // 2
        else:
            print('WINNER! Computer has found your number! it is {}'.format(comp_num))


def f_test():
    for i in range(1, 100, 1):
        print(random.randint(1, 5))
#f_play()
f_hw()
#f_test()
