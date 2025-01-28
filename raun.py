def inserir():
    while True:
        try:
            nota = float(input(f'Digite uma nota entre 0 e 10: '))
            if 0 <= nota <=10:
                print(f'Você digitou uma nota válida, que foi a {nota}')
                break
            else:
                print(f'Você digitou uma nota inválida. Reveja seu input.')
        except ValueError:
            print(f'Você digitou um input inválido')
inserir()
