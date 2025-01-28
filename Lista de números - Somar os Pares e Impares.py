números = [21, 5, 34, 8, 16, 7, 3]

def verificar_par (números):
    soma_pares = 0
    for numero in números:
        if numero % 2 == 0:
            soma_pares = soma_pares + numero
    return soma_pares

def verificar_impar(números):
    soma_impares = 0
    for numero in números:
        if numero % 2 == 1:
            soma_impares = soma_impares + numero
    return soma_impares

def main():
    soma_par = verificar_par (números)
    soma_impar = verificar_impar (números)
    return print(f'A soma dos números pares foi de {soma_par}, e a soma dos números ímpares foi de {soma_impar}')

main ()