def coletar_dados():
    cidade = []
    veiculos_passeio = []
    numero_acidentes = []
    for i in range(5):
            cidade.append(int(input(f'Digite o código da cidade: ')))
            veiculos_passeio.append(int(input(f'Digite o número de veículos de passeio da cidade {i+1}: ')))
            numero_acidentes.append(int(input(f'Digite o número de acidentes na cidade {i+1}: ')))
    return cidade, veiculos_passeio, numero_acidentes

def indice (cidade, veiculos_passeio, numero_acidentes):
    max_acidente = max(numero_acidentes)
    min_acidente = min(numero_acidentes)
    med_veiculos = sum(veiculos_passeio) / len(veiculos_passeio)
    max_index = numero_acidentes.index(max_acidente)
    min_index = numero_acidentes.index(min_acidente)
    min_cidade = cidade[min_index]
    max_cidade = cidade[max_index]
    acidentes_menos_2000 = [
        numero_acidentes[i]
        for i in range(len(veiculos_passeio))
        if veiculos_passeio[i] < 2000
    ]
    if acidentes_menos_2000:
        media_acidentes_menos_2000 = sum (acidentes_menos_2000) / len(acidentes_menos_2000)
    else:
        media_acidentes_menos_2000 = 0

    return (
        max_cidade,
        max_acidente,
        min_cidade,
        min_acidente,
        med_veiculos,
        media_acidentes_menos_2000
    )
       

def main (): 
    cidades, veiculos_passeio, numero_acidentes = coletar_dados()
    (
        max_cidade,
        max_acidente,
        min_cidade,
        min_acidente,
        med_veiculos,
        media_acidentes_menos_2000
    ) = indice(cidades, veiculos_passeio, numero_acidentes)
    print(f'Seguem os resultados: ')
    print(f'O maior índice de acidentes de trânsito pertence à cidade {max_cidade}, sendo seu maior índice de {max_acidente}')
    print(f'O menor índice de acidentes pertence à cidade {min_cidade}, sendo seu menor índice de {min_acidente}')
    print(f'A média de veículos nas cinco cidades juntas é de {med_veiculos}')
    print(f'A média de acidentes de trânsito nas cidades com menos de 2000 veículos de passeio é de {media_acidentes_menos_2000}')

main()