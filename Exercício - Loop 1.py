def inserir():
    while True:
        try:
            nota = float(input(f'Digite uma nota entre 0 a 10: '))
            if 0 <= nota <= 10:
                print(f'Você digitou uma nota válida, sendo {nota}')
                break
            else:
                print(f'Valor inválido. A nota deve estar entre 0 e 10.')
        except ValueError:
            print(f'Entrada inválida. Digite um número válido.')
inserir()   