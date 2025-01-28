numeros = []
alturas = []

for i in range(1, 11):
    numeros.append(int(input(f'Digite o número do aluno {i}: ')))
    alturas.append(int(input(f'Digite a altura do aluno {i}: ')))

altura_max = max(alturas)
altura_min = min(alturas)
indice_max = alturas.index(altura_max)
indice_min = alturas.index(altura_min)
numero_max = numeros[indice_max]
numero_min = numeros[indice_min]

print (f'A aluno mais alto é o aluno de número {numero_max}, que possui a altura de {altura_max}. O aluno mais baixo é o aluno {numero_min}, que possui a altura de {altura_min}')