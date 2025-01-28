def input_eleitores():
    numero_eleitores = int(input(f'Digite o número total de eleitores: '))
    return numero_eleitores

def voto(numero_eleitores):
    voto_a = 0
    voto_b = 0
    voto_c = 0
    for i in range (numero_eleitores):
        voto = int(input(f'Registre seu voto no candidato A votando "1", B votando "2" ou C votando "3": '))
        if voto == 1:
            voto_a = voto_a + 1
        elif voto == 2:
            voto_b = voto_b + 1
        elif voto == 3:
            voto_c = voto_c + 1
    return voto_a, voto_b, voto_c

def classificar_votos(voto_a, voto_b, voto_c):
    votos = {'A': voto_a, 'B': voto_b, 'C': voto_c}
    votos_ordenados = sorted(votos.items(), key=lambda item: item[1], reverse=True )
    return votos_ordenados

def main():
    eleitores = input_eleitores()
    voto_a, voto_b, voto_c = voto(eleitores)
    votos_classificados = classificar_votos(voto_a, voto_b, voto_c)
    for i, (candidato, votos) in enumerate(votos_classificados, start = 1):
        print (f'{i}º lugar: Candidato {candidato} com {votos} votos')
    

main ()
    
    


    
        