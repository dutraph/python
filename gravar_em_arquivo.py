f = open(r'/Users/paulosilva/Documents/python2020/x.txt', 'w')
for linha in range(1, 100):
    f.write(f'{linha}\n')
f.close()