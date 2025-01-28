def menu():
    print (f'Escolha sua operação: 1 = Adição/n 2 = Subtração/n 3 = Divisão/n 4 = Multiplicação')
    operação = int(input())
    if operação == "sair":
        return "sair"
    else:
        return operação
    
def adição ():
    resultado = 0 
    while True:
        adição = input(f'Digite um valor ou "stop" para ver a soma: ')
        if adição.lower() == "stop":
            break
        else: 
            resultado = int(adição) + resultado
    return resultado 


def subtração ():
    valor_primeiro = int(input(f'Digite o primeiro valor: '))
    while True:
        subtração = input(f'Digite um valor para subtrair de {valor_primeiro} ou "stop" para ver a subtração: ')
        if subtração.lower() == "stop":
            break
        else:
            valor_primeiro = valor_primeiro - int(subtração)
    return valor_primeiro


def divisão ():
    valor_primeiro = int(input(f'Digite o primeiro valor a ser dividido: '))
    while True:
        divisão = input(f'Digite um valor para dividir {valor_primeiro} ou "stop" para ver a divisão: ')
        if divisão.lower() == "stop":
            break
        else:
            valor_primeiro = valor_primeiro / int(divisão)
    return valor_primeiro
            

def multiplicação ():
    valor_primeiro = int(input(f'Digite o primeiro valor a ser multiplicado: '))
    while True:
        multiplicação = input(f'Digite um valor para multiplicar {valor_primeiro} ou "stop" para ver a multiplicação: ')
        if multiplicação == "stop":
            break
        else:
            valor_primeiro = valor_primeiro * int(multiplicação)
    return valor_primeiro
    
     

def main():
    while True:
        operação = menu ()
        if operação == "sair":
            break
        if operação == 1:   
            adição_num = adição ()
            print(f'O resultado da adição é {adição_num}')
        elif operação == 2:
            subtração_num = subtração ()
            print(f'O resultado da subtração é {subtração_num}')
        elif operação == 3:
            divisão_num = divisão ()
            print(f'O resultado da divisão é {divisão_num}')
        elif operação == 4:
            multiplicação_num = multiplicação ()
            print(f'O resultado da multiplicação é {multiplicação_num}')
        else:
            print (f'Opção inválida. Tente novamente')
    
main ()


    
    
    
    







    
