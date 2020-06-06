cont = 0
while True:
    num = int(input('Entre uma nota entre 0 e 10: '))
    if num <= 10 and num >= 0:
        print('Nota valida')
        break
    else:
        print('Numero invalido')
        num = num + 1

### outra resoluçao

nota = float(input('Digite uma nota: '))
while nota < 0 or nota > 10:
    print('Notas entre 0 e 10: ')
    nota = float(input('Digite uma nota: '))
