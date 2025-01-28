def inserir ():
    numeros = []
    for i in range(2):
        numeros.append(int(input(f'Digite o número {i + 1}: ')))
    
    inicio = min(numeros)
    fim = max(numeros)

    for numero in range (inicio + 1, fim):
        print(numero)
        
inserir ()