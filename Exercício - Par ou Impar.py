def numero():
    numero = int(input(f'Digite um número inteiro: '))
    if numero % 2 == 0:
        print (f'O número digitado é par.')
    else:
        print (f'O número digitado é impar.')

numero()