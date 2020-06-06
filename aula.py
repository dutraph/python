'''n = int(input('Digite um numero: ')) 
x = 0
while x <= n:
    print(x)
    x = x + 2
'''

n = 1
soma = 0
while n <= 10:
    x = int(input(f'{n} Numero: '))
    soma = soma + x
    n = n + 1
print(f'Soma: {(soma / 10):.1f}')