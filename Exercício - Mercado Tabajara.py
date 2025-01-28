def tipo_quantidade():
    tipo = int(input(f'Digite 1 para Filé Duplo, 2 para Alcatra e 3 para Picanha: '))
    quantidade = float(input(f'Digite a quantidade a ser comprada: '))
    return tipo, quantidade

def file_duplo (quantidade):
    if quantidade <= 5:
        valor = quantidade * 4.90
        return valor
    elif quantidade > 5:
        valor = quantidade * 5.80
        return valor

def alcatra (quantidade):
    if quantidade <= 5:
        valor = quantidade * 5.90
        return valor
    elif quantidade > 5:
        valor = quantidade * 6.80
        return valor

def picanha (quantidade):
    if quantidade <= 5:
        valor = quantidade * 6.90
        return valor
    elif quantidade > 5:
        valor = quantidade * 7.80
        return valor

def main():
    cartão = input(str(f'Possui cartão Tabajara? Responda "sim" ou "não": '))
    try:
        if cartão.lower() == "sim":
            tipo, quantidade = tipo_quantidade()
            file = file_duplo (quantidade) * 0.95
            alca = alcatra(quantidade) * 0.95
            pica = picanha(quantidade) * 0.95
        else:
            tipo, quantidade = tipo_quantidade()
            file = file_duplo (quantidade)
            alca = alcatra(quantidade)
            pica = picanha(quantidade)
    except ValueError:
        print (f'Resposta inválida.')
        return
    if tipo == 1:
        print (f'O preço total é de {file:.2f} reais, sendo {quantidade} KG de filé duplo.')
    elif tipo == 2:
        print (f'O preço total é de {alca:.2f} reais, sendo {quantidade} KG de alcatra.')
    elif tipo == 3:
        print (f'O preço total é de {pica:.2f} reais, sendo {quantidade} KG de picanha.')

main ()
    


