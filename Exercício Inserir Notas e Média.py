def inserir_notas():
    notas = []
    for i in range (4):
        notas.append(int(input(f'Digite uma nota: ')))
    return notas

def média_num (notas):
    média = sum(notas) / len (notas)
    return média

def main ():
    notas = inserir_notas()
    média = média_num(notas)
    return print(f'A média das notas {notas} é {média}')

main ()