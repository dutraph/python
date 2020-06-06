import getpass
#cont = 0
while True:
    user = input('Digite seu nome de usuario: ')
    senha = getpass.getpass('Digite sua senha: ')
    if user != senha:
        print(f'Bem Vindo {user}')
        break
    else:
        print('Erro! A senha nao deve ser igual ao nome do usuario, tente outra vez.', end='\n\n')


### outra resoluçao
'''
usuario = input('Usuario: ')
senha = input('Senha: ')
while usuario == senha:
    print('Senha deve ser diferente do usuario')
    usuario = input('Usuario: ')
    senha = input('Senha: ')
'''