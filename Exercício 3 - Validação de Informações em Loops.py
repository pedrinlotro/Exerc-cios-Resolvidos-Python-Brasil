def inserir():
    while True:
        try:
            nome = input(f'Digite seu nome: ')
            if len(nome) > 3:
                print(f'Nome válido')
                break
            else:
                print (f'Nome inválido. Digite novamente.')
        except ValueError:
            print (f'Input incorreto. Reveja.')
    
    while True:
        try:
            idade = int(input(f'Digite sua idade: '))
            if 0 < idade < 100:
                print (f'Idade válida.')
                break
            else:
                print(f'Idade inválida. Digite novamente.')
        except ValueError:
            print(f'Digite um input válido')
    
    while True:
        try:
            salario = int(input(f'Digite seu salário: '))
            if salario > 0:
                print (f'Salário válido.')
                break
            else:
                print(f'Salário inválido. Digite um maior que zero.')
        except ValueError:
            print(f'Input inválido.')
    
    while True:
        try:
            sexo = input(f'Digite seu sexo (m para mulher e h para homem): ')
            if sexo.lower() in ['h', 'm']:
                print (f'Sexo válido.')
                break
            else:
                print(f'Sexo inválido. Reveja o que digitou.')
        except ValueError:
            print (f'Input inválido.')

    while True:
        try:
            estado_civil = input(f'Digite seu estado civil: s ou v: ')
            if estado_civil.lower() == 's' or 'v':
                print(f'Estado Civil válido.')
                break
            else:
                print(f'Estado civil inválido')
        except ValueError:
            print (f'Input inválido.')

    print (f'Seu nome é {nome}, sua idade é de {idade} anos, seu salário é {salario} reais, seu sexo é {sexo}, seu estado civil é {estado_civil}')

inserir()