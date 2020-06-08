k = 1
nota = 0
soma = 0
while k <= 4:
    nota = float(input(f'Digite a {k} nota: '))
    k = k + 1
    soma = soma + nota
    media = soma / (k-1)

if media < 7:
    print(f'Reprovado, sua media eh {media:.1f}.')
elif media == 10:
    print(f'Aprovado, com Distincao, Sua media eh de {media:.1f}.')
else:
    print(f'Aprovado, sua media eh {media:.1f}') 
