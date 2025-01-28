def input_cds():
    quantidade = int(input(f'Digite a quantidade de CDS: '))
    valor_total = 0
    coleção = []
    for i in range (quantidade):
        nome_cd = input(f'Digite o nome do CD {i + 1}: ')
        valor_cd = float(input(f'Digite o valor do CD {i + 1}: '))
        coleção.append((nome_cd, valor_cd))
        valor_total = valor_total + valor_cd

    valor_medio = valor_total / quantidade

    print (f'O valor total é de {valor_total} reais e o valor médio investido é de {valor_medio} reais')


input_cds()

    