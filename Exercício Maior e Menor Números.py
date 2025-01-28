def inserir_números ():
    números = []
    for i in range (2):
        números.append(int(input(f'Digite um número inteiro: ')))
    return números

def num_máximo(números):
    return max(números)

def num_mínimo(números):
    return min(números)

def main ():
    numeros = inserir_números()
    maximo = num_máximo(numeros)
    minimo = num_mínimo(numeros)
    return print(f'O maior número digitado foi o {maximo} e o menor foi o {minimo}')

main ()
    