def inserir_sexo ():
    sexo = input(f'Digite se você é homem ou mulher: ')
    return sexo

def inserir_altura():
    altura = float(input(f'Digite sua altura em cm: '))
    return altura

def calcular_homem(altura):
    peso_homem = (altura * 72.7) - 58
    return peso_homem

def calcular_mulher(altura):
    peso_mulher = (altura * 62.1) - 44.7
    return peso_mulher

def main():
    sexo = inserir_sexo()
    altura = inserir_altura ()
    if sexo.lower() == "homem":
        peso = calcular_homem(altura)
    else:
        peso = calcular_mulher(altura)
    print (f'O peso ideal para um(a) {sexo} de {altura} cm é {peso:.2f} kg')
    return

main()


