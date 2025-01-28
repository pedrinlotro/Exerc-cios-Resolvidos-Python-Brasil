import math
def equação_segundo_grau ():
    a = float(input(f'Digite o valor de A: '))
    if a == 0:
        print(f'Se o valor de A é 0, a equação não é de segundo grau.')
        return
    b = float(input(f'Digite o valor de B: '))
    c = float(input(f'Digite o valor de C: '))

    delta = b**2 - 4*a*c

    if delta < 0:
        print(f'A equação não possui raízes reais')
    elif delta == 0:
        raiz = -b / (2 * a)
        print (f'A equação possui apenas uma raiz real {raiz}')
    
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f'A equação possui duas raízes reais: {raiz1} e {raiz2}')

equação_segundo_grau()
