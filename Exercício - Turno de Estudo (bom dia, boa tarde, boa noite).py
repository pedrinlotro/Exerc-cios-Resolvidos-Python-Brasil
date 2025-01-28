def inserir_turno():
        turno = (input(f'Digite o turno em que você estuda: M-matutino ou V-Vespertino ou N- Noturno: '))
        if turno.lower() == "m":
            print(f'Bom dia!')
        elif turno.lower() == "v":
            print (f'Boa tarde!')
        elif turno.lower() == "n":
            print (f'Boa noite!')
        else:
            print (f'O que você digitou é inválido.')

inserir_turno ()



    