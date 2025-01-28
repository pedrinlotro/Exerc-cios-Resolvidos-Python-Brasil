def inserir():
    tipo = int(input(f'Digite 1 para Gasolina e 2 para Álcool: '))
    litros = int(input(f'Digite quantos litros deseja colocar: '))
    return tipo, litros

def gasolina (litros):
    litros_valor = litros * 2.50
    litros_20_menos = litros_valor * 0.96
    litros_20_mais = litros_valor * 0.94
    if litros <= 20:
        return litros_20_menos
    elif litros > 20:
        return litros_20_mais

def alcool (litros):
    alcool_valor = litros * 1.90
    alcool_20_menos = alcool_valor * 0.97
    alcool_20_mais = alcool_valor * 0.95
    if litros <= 20:
        return alcool_20_menos
    elif litros > 20:
        return alcool_20_mais
    
def main ():
    tipo, litros = inserir()
    gaso = gasolina (litros)
    alco = alcool (litros)
    if tipo == 1:
        return print(f'O preço a ser pago é de {gaso} reais')
    elif tipo == 2:
        return print (f'O preço a ser pago é de {alco} reais')
        
main ()
    