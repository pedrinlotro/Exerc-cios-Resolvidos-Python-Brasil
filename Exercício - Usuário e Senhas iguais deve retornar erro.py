def inserir():
    while True:
        try:
            usuario = input(f'Digite o nome de usuário: ')
            senha = input(f'Digite sua senha: ')
            if usuario != senha:
                print (f'Tudo certo com seu login.')
                break
            else:
                print (f'Sua senha e seu login são iguais. Reveja o que digitou.')
        except ValueError:
            print(f'Input incorreto.')

inserir()

