def perguntas():
    contador = 0
    pergunta_1 = input(f'Responda com "sim" ou "não"! Telefonou para a vítima?: ')
    pergunta_2 = input(f'Responda com "sim" ou "não"! Esteve no local do crime?: ')
    pergunta_3 = input(f'Responda com "sim" ou "não"! Mora perto da vítima? ')
    pergunta_4 = input(f'Responda com "sim" ou "não"! Devia para a vítima? ')
    pergunta_5 = input(f'Responda com "sim" ou "não"! Já trabalhou com a vítima? ')

    if pergunta_1.lower() == "sim":
        contador = contador + 1
    if pergunta_2.lower() == "sim":
        contador = contador + 1
    if pergunta_3.lower() == "sim":
        contador = contador + 1
    if pergunta_4.lower() == "sim":
        contador = contador + 1
    if pergunta_5.lower() == "sim":
        contador = contador + 1

    if contador == 2:
        print (f'Você é suspeito(a) do crime.')
    elif contador in [3, 4]:
        print (f'Você é cúmplice(a) do crime.')
    elif contador == 5:
        print(f'Você é o assassino(a).')
    else: 
        print (f'Você é inocente')

perguntas ()

