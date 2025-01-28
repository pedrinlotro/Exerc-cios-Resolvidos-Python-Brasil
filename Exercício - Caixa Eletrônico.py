def saque ():
    saque = int(input(f'Digite o valor do saque (mínimo de 10 e máximo de 600): '))
    if saque < 10 or saque > 600:
        print(f'Valor inválido.')
        return
    notas_disponiveis = [100, 50, 10, 5, 1]
    notas_utilizadas = {}

    for nota in notas_disponiveis:
        if saque >= nota:
            quantidade = saque // nota
            saque %=nota
            notas_utilizadas[nota] = quantidade

    print("Notas fornecidas:")
    for nota, quantidade in notas_utilizadas.items():
        if quantidade > 0:
            print(f"{quantidade} nota(s) de R$ {nota}")
    
saque ()

