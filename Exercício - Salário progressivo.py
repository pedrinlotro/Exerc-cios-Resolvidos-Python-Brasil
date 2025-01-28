def calcular_salario(salario_inicial, ano_atual):
    ano_contratacao = 1995
    aumento = 1.5 / 100
    salario_atual = salario_inicial

    for ano in range(ano_contratacao + 1, ano_atual + 1):
        salario_atual = salario_atual + salario_atual * aumento
        aumento = aumento * 2

    return salario_atual

def main():
    salario_inicial = int(input(f'Digite o salário inicial do funcionário: '))
    ano_atual = int(input(f'Digite o ano atual: '))
    salario_final = calcular_salario(ano_atual, salario_inicial)
    print(f'O salário do funcionário no ano de {ano_atual} é de {salario_final:.2f} reais')

main()