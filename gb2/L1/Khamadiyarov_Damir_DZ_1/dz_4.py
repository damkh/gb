#num = int(input('Enter your number: '))
num = 2318328301
print(num)
global_max = 0
while num // 10 != 0:
    element = num % 10
    local_max = (num % 100) // 10
    if element > local_max:
        local_max = element
    if local_max > global_max:
        global_max = local_max
    num = num // 10

print(f'global_max = {global_max}')