print('Checando a existencia dos triangulos!')
a = int(input('Entre o lado a: '))
b = int(input('Entre o lado b: '))
c = int(input('Entre o lado c: '))

ab = a + b
bc = b + c
ac = a + c

con1 = ((bc - ac) < ab < (bc + ab))
con2 = ((bc - ab) < ac < (bc + ab))
con3 = ((ab - ac) < bc < (ab + ac))

if con1 is True and con2 is True and con3 is True:
    print('Triangulo valido')
    if a == b == c:
        print('Triangulo Equilatero')
    elif a != b != c:
        print('Triangulo Escaleno')
    else:
        print('Triangulo Isosceles')
else:
    print('Nao é um triangulo valido')