codigos = []
alturas = []
pesos = []
while True:
    codigo = int(input(f'Digite o código do cliente ou 0 para parar: '))
    if codigo == 0:
        break
    codigos.append(codigo)
    alturas.append(int(input(f'Digite a altura do cliente em centímetros: ')))
    pesos.append(int(input(f'Digite o peso do cliente em kg: ')))
max_altura = max(alturas)
min_altura = min(alturas)
max_peso = max(pesos)
min_peso = min(pesos)
med_altura = sum(alturas) / len(alturas)
med_peso = sum(pesos) / len(pesos)
cliente_a_max = codigos[alturas.index(max_altura)]
cliente_a_min = codigos[alturas.index(min_altura)]
cliente_p_max = codigos[pesos.index(max_peso)]
cliente_p_min = codigos[pesos.index(min_peso)]
print (f'A maior altura é {max_altura}, do cliente {cliente_a_max}, a menor é {min_altura}, do cliente {cliente_a_min} o maior peso é {max_peso}, do cliente {cliente_p_max} o menor é {min_peso}, do cliente {cliente_p_min}. A média das alturas é {med_altura:.2f} e a média dos pesos é {med_peso:.2f}')

    