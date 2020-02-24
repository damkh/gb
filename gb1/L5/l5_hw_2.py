import random

def rand_elem(list):
    random.seed()
    # return list[random.randint(0, len(list) - 1)]
    if list:
        return random.choice(list)

    if __name__ == '__main__':
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #my_list = []
        print(len(my_list))
        print(random(len(my_list)))
        print(rand_elem(my_list))