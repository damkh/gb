num = 2318328301
#num = int(input('Enter your number: '))
print(f'Your number is: {num}')
global_max = 0
if num > 0:
    while num // 10 != 0:
        element = num % 10
        local_max = (num % 100) // 10
        if element > local_max:
            local_max = element
        if local_max > global_max:
            global_max = local_max
        num = num // 10
    print(f'Max digit is: {global_max}')
else:
    print('Should be positive integer')
