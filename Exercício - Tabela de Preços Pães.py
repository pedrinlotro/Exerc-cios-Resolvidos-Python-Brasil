def pão ():
    preço_unitário = float(input(f'Digite o valor unitário do pão: '))

    for i in range (1, 51):
        valor_total = i * preço_unitário
        print(f'Para {i} pão(es), o valor é de {valor_total}')

pão ()