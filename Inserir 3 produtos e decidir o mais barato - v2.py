def inserir_produtos():
    produtos = []
    for i in range (3):
        produtos.append(str(input(f'Digite o nome do produto {i+1}: ')))
    return produtos

def inserir_preço():
    preços = []
    for i in range(3):
        preços.append(float(input(f'Digite o preço do produto {i+1}: ')))
    return preços

def main ():
    nome_produtos = inserir_produtos()
    preço_produtos = inserir_preço()
    valor_mais_barato = min(preço_produtos)
    indice_barato = preço_produtos.index(valor_mais_barato)
    produto_mais_barato = nome_produtos[indice_barato]
    print(f'O produto mais barato é o {produto_mais_barato}')

main ()
    