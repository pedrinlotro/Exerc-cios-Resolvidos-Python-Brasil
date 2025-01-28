números = [54, 10, 29, 87, 7, 64]

def num_max (números):
    return max(números)

def num_min(números):
    return min(números)

def main():
    maximo = num_max(números)
    minimo = num_min(números)
    lista = números

    return print(f'O maior valor da lista {lista} é {maximo}, e o menor valor é {minimo}')

main ()