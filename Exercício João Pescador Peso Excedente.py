def inserir_peso():
    peso = float(input(f'Digite o peso coletado em kg: '))
    return peso

def regra(peso):
    if peso > 50:
        multa = (peso - 50) * 4
        return multa
    else:
        return None

def main():
    peso = inserir_peso()
    multa = regra(peso)
    if multa is None:
        print(f'O peso limite não foi excedido, e, portanto, não há multa')
    else:
        return print(f'Para o peso de {peso}, a multa foi de {multa} reais')

main()



