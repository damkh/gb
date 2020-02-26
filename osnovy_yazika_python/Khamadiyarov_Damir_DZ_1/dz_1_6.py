a = 2
b = 3
#a = int(input('Enter first day result (km): '))
#b = int(input('Enter limit distance (km): '))

day = 1
print(f'Day {day} result is: {round(a, 2)} km')
while a < b:
    a += a*0.1
    day += 1
    print(f'Day {day} result is: {round(a, 2)} km')
print(f'\033[1mOn day {day} the athlete achieved a result of at least {b} km.\033[0m')
