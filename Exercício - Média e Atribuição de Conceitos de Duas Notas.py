def inserir_notas():
    notas = []
    for i in range (2):
        while True:
            try:
                nota = float(input(f'Digite a nota {i + 1}, entre 0 e 10: '))
                if nota <= 10 and nota >= 0:
                    notas.append(nota)
                    break
                else:
                    print(f'Valor inválido!')
            except ValueError:
                print(f'Valor inválido!')
    return notas

def classificação (notas):
    média = sum(notas) / len(notas)
    if média >= 9:
        print (f'Seu conceito é A, você está aprovado com média {média}')
    elif média >= 7.5 and média < 9:
        print (f'Seu conceito é B, você está aprovado com média {média}')
    elif média >= 6 and média < 7.5:
        print (f'Seu conceito é C, você está aprovado com média {média}')
    elif média >= 4 and média < 6:
        print (f'Seu conceito é D, você está reprovado com média {média}')
    elif média >= 0 and média < 4:
        print (f'Seu conceito é E, você está reprovado com média {média}')
    return média
    
def main():
    notas = inserir_notas()
    return classificação(notas)

main ()


    
        


        