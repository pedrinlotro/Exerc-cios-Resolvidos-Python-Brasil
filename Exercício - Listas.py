def inserir_nota():
    notas = []
    contador = 1
    while contador < 5:
        notas.append(float(input(f'Digite uma nota: ')))
        contador = contador + 1
    return notas

def nota_max(notas):
    return max(notas)

def nota_min(notas):
    return min(notas)

def média (notas):
    return sum(notas) / len (notas)

def main ():
    notas = inserir_nota ()
    maior_nota = nota_max(notas)
    menor_nota = nota_min(notas)
    media = média(notas)
    print(f'A média final é {media}, a maior nota é {maior_nota}, e a menor nota é {menor_nota}')

main ()