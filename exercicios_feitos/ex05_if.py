k = 1
nota = 0
soma = 0
while k <= 4:
    nota = int(input(f'Digite a {k} nota: '))
    k = k + 1
    soma = soma + nota
    media = soma / (k-1)

if media < 7:
    print(f'Reprovado, sua media eh {media}.')
elif media == 10:
    print(f'Aprovado, com Distincao, Sua media eh de {media}.')
else:
    print(f'Aprovado, sua media eh {media}') 
