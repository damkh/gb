age = int(input('Age: '))
mass = int(input('Mass: '))

if age <= 30 and 50 < mass < 120:
    print('good')
elif 50 > mass or mass > 120:
    if age > 30:
        if age > 40:
            print('doctor')
        else:
            print('run')
    else:
        print('xz-1')
else:
    print('xz-2')
