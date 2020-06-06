km = int(input('Qual sua velocidade Km/h: '))
ex = km - 110
if km >= 111:
    print(f'Voce excedeu a velocidade em {ex} Km/h')
    print(f'Sua multa por excesso de velocidade é: R${(ex * 5):.2f}') 
else:
    print('Voce esta dentro do limite!')