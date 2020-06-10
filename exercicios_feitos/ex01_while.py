while True:
    n = int(input('Entre um numero entre 0 e 10: '))
    if n > 10 or n < 0:
        print('Entre um numero valido...',end='\n\n')
    else:
        print(f'Parabens voce digitou {n}, um numero valido.')
        break        