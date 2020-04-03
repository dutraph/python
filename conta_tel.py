# Primeiro programa basico em python

minutos = int(input("Minutos utilizados: "))
if minutos < 200:
    preco = 0.20
    print ('Tarifa %.2f' %preco)
elif minutos <= 400:
    preco = 0.18
    print ('Tarifa %.2f' %preco)
elif minutos < 800:
    preco = 0.15
    print ('Tarifa %.2f' %preco)
else:
    preco = 0.08
    print ('Tarifca promocional aplicada')
print ("Conta telefonica: R$ %.2f" % (minutos * preco))
