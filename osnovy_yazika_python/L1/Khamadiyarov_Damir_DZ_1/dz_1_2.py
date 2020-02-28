seconds = 86400
print('342342 should be 95:5:42')
print('86400 should be 24:0:0')
#seconds = int(input('Enter time in seconds: '))
print(f'{seconds} seconds is: {seconds // 3600}:{(seconds - (seconds // 3600) * 3600) // 60}:{seconds % 60}')