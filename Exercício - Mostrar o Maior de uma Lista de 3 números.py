def inserir_números():
    números = []
    for i in range (3):
        números.append(int(input(f'Digite um número: ')))
    return números

def máximo (número):
    return max(número)

def mínimo(número):
    return min(número)

def main():
    números = inserir_números()
    maior = máximo(números)
    menor = mínimo(números)
    print(f'Da lista {números} o maior é {maior} e o menor é {menor}')

main()