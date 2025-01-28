def inserir_salario ():
    salario = int(input(f'Digite o salário: '))
    return salario

def cálculos(salario):
    if salario >= 280:
        salario = salario * 1.2
    elif salario > 280 and salario < 700:
        salario = salario * 1.15
    elif salario > 700 and salario < 1500:
        salario = salario * 1.10
    elif salario > 1500:
        salario = salario * 0.5
    return salario
   
def main ():
    salario_antes = inserir_salario()
    salario_depois = cálculos (salario_antes)
    valor_aumento = (salario_depois) - (salario_antes)
    return print (f'O salário antes do reajuste é {salario_antes} reais, o novo salário é {salario_depois} reais, e o aumento foi de {valor_aumento} reais')

main ()

