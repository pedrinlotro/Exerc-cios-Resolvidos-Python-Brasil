numero = []
for i in range(5):
    numero.append(int(input(f'Digite o número {i + 1}: ')))
    media = sum(numero) / len(numero)
    soma = sum(numero)
print (f'A média dos números é {media}, e sua soma é {soma}')
