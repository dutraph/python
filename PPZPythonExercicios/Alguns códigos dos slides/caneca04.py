import urllib.request
pagina = urllib.request.urlopen(
    'http://beans.itcarlow.ie/prices-loyalty.html') 
texto = pagina.read().decode('utf8') 
onde = texto.find('>$')
inicio = onde + 1
fim = inicio + 5
preço = texto[inicio:fim]
print (preço)

