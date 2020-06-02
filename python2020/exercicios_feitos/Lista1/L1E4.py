print('Calculo de aumento salarial!')
sal = float(input("Entre o valor do seu salario, R$ "))
porc = float(input("Entre o percentual de aumento %: "))
aumento  = ((porc / 100)  * sal)
nov_sal = aumento + sal
print(f"Seu salario apos o aumento é: R${nov_sal:.2f}")
print(f'Seu aumento foi de R${aumento:.2f} ')