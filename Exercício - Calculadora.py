def inserir_numeros():
    numeros = []
    for i in range(2):
        numeros.append(float(input(f'Digite o número {i + 1}: ')))
    return numeros

def calcular(numeros):
    print (f'Escolha uma operação: Adição = 1, Subtração = 2, Multiplicação = 3, Divisão = 4')
    operação = int(input(f'Digite o número da operação a ser realizada: '))
    if operação == 1:
        resultado = numeros [0] + numeros [1]
        operacao_str = "adição"
        return resultado, operacao_str
    
    elif operação == 2:
        resultado = numeros [0] - numeros [1]
        operacao_str = "subtração"
        return resultado, operacao_str

    elif operação == 3:
        resultado = numeros [0] * numeros [1]
        operacao_str = "multiplicação"
        return resultado, operacao_str
    
    elif operação == 4:
        resultado = numeros [0] / numeros [1]
        operacao_str = "divisão"
        return resultado, operacao_str
    
    else:
        print(f'Número de operação inválido.')
        return
    
def main ():
    numeros = inserir_numeros()
    resultado, operação_str = calcular(numeros)
    if resultado is not None:
        tipo_numero = "inteiro" if resultado.is_integer() else "decimal"
        paridade = "par" if resultado % 2 == 0 else "ímpar"
        sinal = "positivo" if resultado > 0 else "negativo" if resultado < 0 else "neutro"
        return print(f"O resultado da operação {operação_str} é {resultado}, esse número é {tipo_numero}, {paridade} e {sinal}")

main ()




