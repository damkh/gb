#seconds = int(input('Enter time in seconds: '))
seconds = 342342
print('342342 should be 95:05:42')
print(f'{seconds} seconds is: {seconds // 3600}:{(seconds - (seconds // 3600) * 3600) // 60}:{seconds % 60}')