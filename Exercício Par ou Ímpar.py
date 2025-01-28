def par_ou_impar (numero):
    if numero % 2 == 0:
        return f'O número {numero} é par'
    return f'O número {numero} é impar'
def main ():
    numero = int(input('Informe um número inteiro qualquer: '))
    print (par_ou_impar (numero))

main ()