minutos = int(input('Entre os minutos usados durante o mes: '))
if minutos < 200:
    print('Tarifa normal de R$ 0,20/min', end='\n\n')
    print(f'Seu gasto esse mes foi de R$ {(minutos * 0.20):.2f}')
elif minutos >= 200 and minutos < 400:
    print('Tarifa promocional de R$ 0,18/min', end='\n\n')
    print(f'Seu gasto esse mes for de R$ {(minutos * 0.18):.2f}')
elif minutos < 800:
    print('Tarifa super promocional de R$ 0,15/min', end='\n\n')
    print(f'Seu gasto esse mes foi de R$ {(minutos * 0.15):.2f}')
else:
    print('Tarifa ultra promocional de R$ 0,08/min', end='\n\n')
    print(f'Seu gasto esse mes foi de R$ {(minutos * 0.08):.2f}')