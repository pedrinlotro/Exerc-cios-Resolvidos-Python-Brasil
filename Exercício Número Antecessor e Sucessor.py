def inserir_número():
    número = int(input(f'Digite um número inteiro: '))
    return número

def sucessor_num (número):
    sucessor = número + 1
    return sucessor

def antecessor_num (número):
    antecessor = número - 1
    return antecessor 

def main ():
    número = inserir_número()
    sucessor = sucessor_num(número)
    antecessor = antecessor_num(número)
    return print (f'O número inteiro escolhido foi {número}, seu sucessor é {sucessor} e seu antecessor é {antecessor}')

main ()
