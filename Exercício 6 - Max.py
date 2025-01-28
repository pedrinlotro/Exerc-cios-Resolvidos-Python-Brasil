numero = []
for i in range(5):
    numero.append(int(input(f'Digite o número {i+ 1}: ')))
    num_max = max(numero)
print (f'O maior número é {num_max}')