print('Calculo de desconto de produto!')
prec = float(input("Entre o valor do produto: R$"))
desc = float(input("Entre o percentual de desconto solicitado: "))
val_desc = (prec - (prec * (desc / 100)))
econo = prec - val_desc
print(f'O total de desconto recebido foi: R${econo:.2f}')
print(f'O total a pagar com desconto é: R${val_desc:.2f}')
