def tabela_preços():
    preço_unit = 1.99

    for i in range (1, 51):
        valor_total = i * preço_unit
        print (f'Para a quantidade de {i} item, o preço é de {valor_total} reais')

tabela_preços()