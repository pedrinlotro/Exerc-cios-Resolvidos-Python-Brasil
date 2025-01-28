import math
def inserir_tamanho():
    tamanho = int(input(f'Digite o tamanho da área em metros quadrados: '))
    return tamanho

def tinta_lata(tamanho):
    cobertura_tinta = tamanho / 6
    lata_litros = 18
    lata_preço = 80
    latas_necessárias = math.ceil(cobertura_tinta / lata_litros)
    preço_total_lata = latas_necessárias * lata_preço
    return preço_total_lata, latas_necessárias

def tinta_galão(tamanho):
    cobertura_tinta = tamanho / 6
    galão_litros = 3.6
    galão_preço = 25
    galões_necessários = math.ceil(cobertura_tinta / galão_litros)
    preço_total_galão = galões_necessários * galão_preço
    return preço_total_galão, galões_necessários

def lata_galão_misturados(tamanho):
    cobertura_tinta = tamanho / 6
    lata_litros = 18
    lata_preço = 80
    latas_necessárias = math.ceil(cobertura_tinta / lata_litros)
    tinta_restante = cobertura_tinta - (lata_litros * latas_necessárias)
    galão_litros = 3.6
    galão_preço = 25
    galões_necessários = math.ceil(tinta_restante / galão_litros)
    preço_total_misturado = (latas_necessárias * lata_preço) + (galões_necessários * galão_preço)
    return preço_total_misturado, latas_necessárias, galões_necessários



def main ():
    tamanho = inserir_tamanho ()
    preço_total_lata, latas_necessárias = tinta_lata(tamanho)
    preço_total_galão, galões_necessários = tinta_galão(tamanho)
    preço_total_misturado, latas_necessárias_conjuntas, galões_necessários_conjuntas = lata_galão_misturados(tamanho)
    return print (f'O preço total com latas para a área de {tamanho} metros quadrados é de {preço_total_lata} reais, sendo necessárias {latas_necessárias} latas. Com galões, é de {preço_total_galão}, sendo necessários {galões_necessários} galões. O preço total misturado seria de {preço_total_misturado} reais, sendo necessárias {latas_necessárias_conjuntas} latas e {galões_necessários} galões.')

main ()



