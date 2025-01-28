def inserir ():
    morango = float(input(f'Digite a quantidade a ser comprada de morango, em KG: '))
    maça = float(input(f'Digite a quantidade a ser comparada de maçã, em KG: '))
    return morango, maça

def morangote (morango):
    if morango <= 5:
        valor = morango * 2.50
        return valor
    elif morango > 5:
        valor = morango * 2.20
        return valor

def maçazote (maça):
    if maça <= 5:
        valor = maça * 1.80
        return valor
    elif maça > 5:
        valor = maça * 1.50
        return valor
    

def main ():
    morango, maça = inserir()
    valor_morango = morangote(morango)
    valor_maça = maçazote(maça)
    valor_total = valor_morango + valor_maça
    if morango + maça > 8 or valor_total > 25:
        valor_desconto = valor_total * 0.9
        return print(f'O valor a ser pago é de {valor_desconto:.2f} reais, sendo {valor_morango} reais de morango e {valor_maça} reais de maçã')
    else:
        return print(f'O valor total a ser pago é de {valor_total:.2f} reais, sendo {valor_morango} reais de morango e {valor_maça} reais de maçã')

main()

    