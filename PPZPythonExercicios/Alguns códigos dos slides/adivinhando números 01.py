from random import randint
print ('Bem vindo! Digite um numero entre 1 e 10')
nr = randint(1, 10)
print(nr)
g = int(input('Chute um número: '))
if g == nr:
    print ('Você venceu!')
else:
    print ('Você perdeu!')
print ('Fim do jogo!')

