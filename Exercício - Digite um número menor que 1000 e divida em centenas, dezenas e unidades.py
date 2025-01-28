def inserir_numero():
    numero = int(input(f'Digite um número inteiro menor do que 1000: '))
    if numero > 1000 or numero < 0:
        print(f'Número inválido.')
        return
    
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    resultado = []

    if centenas > 0:
        resultado.append(f"{centenas} {'centena' if centenas == 1 else 'centenas'}")
    if dezenas > 0:
        resultado.append(f"{dezenas} {'dezena' if dezenas == 1 else 'dezenas'}")
    if unidades > 0:
        resultado.append(f"{unidades} {'unidade' if unidades == 1 else 'unidades'}")

    if len(resultado) > 1:
        print(", ".join(resultado[:-1]) + " e " + resultado[-1])
    else:
        print(resultado[0])

inserir_numero()