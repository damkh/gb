# last_num = None
while True:
    last_num = int(input('введите последнее число (от 1 до 100): '))
    if not 1 <= last_num <= 100:
        continue
    print('ввод корректный')
    break

print(last_num ** 2)

