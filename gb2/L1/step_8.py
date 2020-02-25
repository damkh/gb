last_num = int('12')

num = 1
while True:
    if not num % 2:
        print(num)
    num += 1
    if num > last_num:
        break

# TODO continue