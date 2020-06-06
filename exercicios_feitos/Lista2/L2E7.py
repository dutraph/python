import math
m2 = int(input('Quantos Metros quadrados voce quer pintar: '))
latas = math.ceil(m2 / 54)
print (f'Voce ira precisar de {latas} latas, valor no total é: R${(latas * 80):.2f}')
