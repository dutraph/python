peixe_kg = float(input('Entre o peso do peixe: '))

if peixe_kg > 50:
    exce = peixe_kg - 50
    multa = 4 * exce
    print(f'Voce excedeu o peso permitido em {exce:.2f}Kg, sua multa é de R${multa:.2f}.')
else:
    print('Seu peixe esta dentro do peso limite de 50 Kg')