import math

def inserir_metros():
    metros = int(input(f'Digite a área a ser pintada em metros quadrados: '))
    return metros

def main():
    metros = inserir_metros()
    litros_necessários = metros / 3
    litros_lata = 18
    preço_lata = 80
    latas_necessarias = math.ceil(litros_necessários / litros_lata)
    preço_total = int(latas_necessarias) * preço_lata
    return print(f'Para uma área de {metros} metros quadrados, serão necessárias {latas_necessarias:.2f} latas, e o preço total é de {preço_total:.2f} reais.')

main ()

