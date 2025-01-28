def inserir_preço():
    preço_produtos = []
    for i in range (3):
        preço_produtos.append(int(input(f'Digite o preço do produto: {i + 1}:  ')))
    return preço_produtos

def inserir_produto():
    nome_produtos = []
    for i in range (3):
        nome_produtos.append(str(input(f'Digite o nome do produto: {i+1}: ')))
    return nome_produtos

def main():
    produto = inserir_produto()
    preço = inserir_preço()
    menor_preço = min(preço)
    indice_menor = preço.index(menor_preço)
    barato_produto = produto[indice_menor]
    return print(f'O produto mais barato é o {barato_produto}, com o valor de {menor_preço} real(is).')
    
main()