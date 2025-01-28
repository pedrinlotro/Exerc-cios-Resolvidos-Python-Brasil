def classificação ():
    entradas = []
    impar = 0
    par = 0
    for i in range (10):
        numero = int(input(f'Digite o número {i + 1}: '))
        entradas.append(numero)
        if numero % 2 == 0:
            par = par +1
        else:
            impar = impar + 1
    return print (f'A quantidade de números ímpares é de {impar} e a de númneros pares é de {par}')

classificação ()
    