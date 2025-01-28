def notas():
    notas = []
    for i in range (3):
        notas.append(int(input(f'Digite a nota {i+1}: ')))
    média = sum(notas) / len(notas)
    if média >= 7 and média < 10:
        print(f'Você foi aprovado com média {média}.')
    elif média >= 10:
        print(f'Você foi aprovado com distinção, com média {média}.')
    else:
        print(f'Você foi reprovado com média {média}.')
    return

notas ()
    


