a,b,c = input('Entre 3 numeros separados por espaco: ').split()
if a > b and a > c:
    print(f'o numero {a} eh o maior.')
elif b > a and b > c:
    print(f'o numero {b} eh o maior')
else:
    print(f'o {c} eh o maior. ')

if a < b and a < c:
    print(f'o numero {a} eh o menor.')
elif b < a and b < c:
    print(f'o numero {b} eh o menor')
else:
    print(f'o {c} eh o menor. ')
