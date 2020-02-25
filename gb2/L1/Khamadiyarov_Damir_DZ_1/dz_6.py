#a = int(input('Enter first day result (km): '))
a = 2
#b = int(input('Enter limit distance (km): '))
b = 3
day = 1
print(f'{day}\'th day result is: {round(a, 2)} km')
while a < b:
    a += a*0.1
    day += 1
    print(f'{day}\'th day result is: {round(a, 2)} km')
print(f'On {day}\'th day, the athlete achieved a result of at least {b} km.')
