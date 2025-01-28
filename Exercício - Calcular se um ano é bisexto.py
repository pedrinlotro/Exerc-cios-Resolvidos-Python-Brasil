def inserir_ano():
    ano = int(input(f'Digite um ano para verificar se é bisexto: '))
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")

inserir_ano ()