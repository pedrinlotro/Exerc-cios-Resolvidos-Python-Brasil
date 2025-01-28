def tabuada ():
    entrada = int(input(f'Escolha o número entre 1 e 10 para visualizar sua tabuada: '))
    if entrada < 1 or entrada > 10:
        return (f'Digite um número entre um e 10.')
    tabuada = {f"{entrada} x {i}": entrada * i for i in range(1, 11)}
    return tabuada
            

resultado = tabuada()
for chave, valor in resultado.items():
    print(f"{chave} = {valor}")
