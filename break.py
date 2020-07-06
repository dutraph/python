soma = 0 
n = 0
while True:
    x = int(input('n (zero para sair): '))
    if x == 0:
        break
    else:
        n = n + 1
    soma += soma
print(f'Media : {soma / n:.1f}')
