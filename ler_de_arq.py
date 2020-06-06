'''f = open(r'/Users/paulosilva/Documents/python2020/x.txt')
for linha in f.readlines():
    print(linha.strip())
f.close()
'''
## OUTRA MANEIRA

with open(r'/Users/paulosilva/Documents/python2020/x.txt') as f:
    print (f.read())