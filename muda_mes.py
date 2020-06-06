'''dd,mm,aaaa = input('Entre um dia no formato dd/mm/aaaa: ').split('/')
lista_mes1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12' ]
lista_mes = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Sep', 'Out', 'Nov', 'Dez' ]
if mm == lista_mes1[0]:
    print (f'{dd} de {(lista_mes[0])} de {aaaa}')
elif mm == lista_mes1[1]:
    print (f'{dd} de {(lista_mes[1])} de {aaaa}')
elif mm == lista_mes1[2]:
    print (f'{dd} de {(lista_mes[2])} de {aaaa}')
elif mm == lista_mes1[3]:
    print (f'{dd} de {(lista_mes[3])} de {aaaa}')
elif mm == lista_mes1[4]:
    print (f'{dd} de {(lista_mes[4])} de {aaaa}')
elif mm == lista_mes1[5]:
    print (f'{dd} de {(lista_mes[5])} de {aaaa}')
elif mm == lista_mes1[6]:
    print (f'{dd} de {(lista_mes[6])} de {aaaa}')
elif mm == lista_mes1[7]:
    print (f'{dd} de {(lista_mes[7])} de {aaaa}')
else :
    print('valeu')'''

### JEITO CERTO

mes = '''Jan Fev Mar Abr Mai Jun Jul Ago Sep Out Nov Dez'''.split()
d,m,a = input('dd/mm/aaaa: ').split('/')
print(f'{d} de {mes[int(m)-1]} de {a}')