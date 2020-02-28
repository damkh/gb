# last_num = int(input('введите последнее число: '))
last_num = int('12')

num = 1
while True:
    if not num % 2:
        print(num)
    num = num + 1
    if num > last_num:
        break
