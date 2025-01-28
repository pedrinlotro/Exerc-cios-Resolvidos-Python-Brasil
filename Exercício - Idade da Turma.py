def idade ():
    lista = []
    for i in range (10):
        lista.append(int(input(f'Digite a idade da pessoa {i + 1}: ')))
    return lista

def calculo (lista):
    media = sum(lista) / len(lista)
    return media
   

def main ():
    lista = idade()
    media = calculo(lista)
    if media >= 0 and media <= 25:
        return print(f'A turma é jovem, tendo uma média de idade de {media} anos')
    if 60 >= media and media >= 26:
        return print (f'A turma é adulta, tendo uma média de idade de {media} anos')
    if media > 60:
        return print (f'A turma é idosa, com uma média de idade de {media} anos')
    

main()
    
    
    


