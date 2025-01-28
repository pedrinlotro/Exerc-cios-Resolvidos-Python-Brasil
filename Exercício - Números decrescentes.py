def inserir_numeros():
    numeros = []
    for i in range (3):
        numeros.append(int(input(f'Digite o número {i+1}: ')))
    numeros.sort(reverse=True)
    return print (f'A ordem decrescente é {numeros}')

inserir_numeros ()


