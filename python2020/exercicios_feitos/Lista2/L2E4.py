n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
n3 = int(input('Terceiro numero: '))

if n1 > n2 and n1 > n3:
    print(f'O numero {n1} é o maior!')
elif n2 > n1 and n2 > n3:
    print(f'O numero {n2} é o maior!')
else:
    print(f'O numero {n3} é o maior!')