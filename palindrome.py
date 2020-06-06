while True:
    palavra = input('Digite uma palavra: ')
    if palavra == palavra[::-1]:
        print('A palavra é Palindrome!')
        break

    else:
        print('Tente outra!',end='\n\n')
       