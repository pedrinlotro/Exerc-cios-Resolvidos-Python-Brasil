def notas_alunos():
    notas = []
    for i in range(2):
        notas.append(float(input(f'Digite a nota: ')))
    return notas

def classificação (notas):
    média = sum(notas) / len(notas)
    if média >= 7:
        print(f'Aprovado com média {média}')
    elif média < 7:
        print (f'Reprovado com média {média}')
    elif média == 10:
        print(f'Aprovado com nota máxima')

def main ():
    notas = notas_alunos()
    classificação (notas)

main ()
