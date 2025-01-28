def inserir_nota():
    notas = []
    contador = 1
    while contador < 5:
        notas.append(int(input(f'Digite uma nota: ')))
        contador = contador + 1
    return notas
    
def calcular_aprovação(notas):
    média = sum (notas) / len (notas)
    if média >= 7:
        print (f'Aprovado com média {média}')
        return
    else:
        nota_final = int(input(f'Reprovado até o momento com média {média} Digite a nota final: '))
        notas.append(nota_final)
        média = sum (notas) / len (notas)
    if média >= 5:
        print (f'Aprovado com média {média}')
    else:
        print (f'Reprovado com média {média}')

def main ():
    notas = inserir_nota()
    calcular_aprovação(notas)

main ()
