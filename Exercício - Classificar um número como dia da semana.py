def inserir_numero():
    numero = int(input(f'Digite um número entre 1 e 7: '))
    return numero

def classificacao(numero):
    if numero == 1:
        print(f'O número 1 representa Domingo!')
    elif numero == 2:
        print(f'O número 2 representa Segunda!')
    elif numero == 3:
        print(f'O número 2 representa Terça!')
    elif numero == 4:
        print(f'O número 2 representa Quarta!')
    elif numero == 5:
        print(f'O número 2 representa Quinta!')
    elif numero == 6:
        print(f'O número 2 representa Sexta!')
    elif numero == 7:
        print(f'O número 2 representa Sábado!')
    else:
        print(f'Valor inválido. O input deve ser um número entre 1 a 7')
    return numero

def main():
    numero = inserir_numero()
    classificação = classificacao(numero)
    return classificação

main ()

    
