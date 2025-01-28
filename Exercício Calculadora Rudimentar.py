def menu():
    print (f'Escolha sua operação: 1 = Adição/n 2 = Subtração/n 3 = Divisão/n 4 = Multiplicação')
    operação = int(input())
    return operação
    

def adição ():
    valor_um = int(input('Adicione um valor: '))
    valor_dois = int(input('Digite o segundo valor: '))
    adição = valor_um + valor_dois
    return adição

def subtração ():
    valor_um = int(input('Digite o primeiro valor: '))
    valor_dois = int(input('Digite o segundo valor: '))
    subtração = valor_um - valor_dois
    return subtração

def divisão ():
    valor_um = int(input('Digite o primeiro valor: '))
    valor_dois = int(input('Digite o segundo valor: '))
    divisão = valor_um / valor_dois
    return divisão

def multiplicação ():
    valor_um = int(input('Digite o primeiro valor: '))
    valor_dois = int(input('Digite o segundo valor: '))
    multiplicação = valor_um * valor_dois
    return multiplicação

def main():
    operação = menu ()
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
        print (f'Opção inválida')
    
main ()


    
    
    
    







    
