'''print('Calculo de tempo de vida perdido de um fumante!', end='\n\n')
cig = int(input('Quantidade de cigarros fumados por dia: ')) # cada cigarro fumado = - 10 min de vida
anos = int(input('Fuma a quantos anos: ')) # 1 ano = 365 dias
tmp_perd = round(((anos * 365) * (cig * 10) / 86400))
print(f'A quantidade de dias perdidos é aproximadamente: {tmp_perd} dias')
'''
## GABARITO MASANORI

''' REGRA DE 3 
1 DIA = 1440 MIN = 144 CIGARROS
'''
cigarros = int(input('Quantidade de cigarros fumados por dia: '))
anos = int(input('Fuma a quantos anos: '))
total_cigarros = anos * 365 * cigarros
dias = total_cigarros / 144
print(f'Voce perdeu {dias:.1f} dias')