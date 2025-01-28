def tamanhos ():
    lista = []
    for i in range (5):
        lista.append(int(input(f'Digite o número {i + 1}: ')))
    maximo = max(lista)
    minimo = min(lista)
    soma = sum(lista)
    return print(f'O maior valor é {maximo}, o menor valor é {minimo}, e a soma dos valores é {soma}')

tamanhos()