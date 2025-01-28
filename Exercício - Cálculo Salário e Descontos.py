def inserir_ganho():
    valor_hora = int(input(f'Digite quantos reais você ganha por dia: '))
    return valor_hora

def inserir_horas():
    horas_trabalhadas = int(input(f'Digite quantos dias você trabalhou no mês: '))
    return horas_trabalhadas

def main():
    horas = inserir_horas()
    valor = inserir_ganho()
    valor_mensal = (horas * valor)
    desconto_ir = valor_mensal * 0.11
    desconto_inss = valor_mensal * 0.08
    desconto_sindicato = valor_mensal * 0.05
    valor_liquido = valor_mensal - (desconto_ir + desconto_inss + desconto_sindicato)
    return print(f'O salário bruto é {valor_mensal} reais, o desconto de IR é {desconto_ir:.2f}, o desconto de INSS é {desconto_inss:.2f} reais, o desconto do sindicato é {desconto_sindicato} reais, e o salário líquido é {valor_liquido} reais')

main ()