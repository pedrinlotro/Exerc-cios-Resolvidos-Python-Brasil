import random

def tentativa ():
    print (f'Bem vindo ao jogo! Você deve adivinhar qual número, entre 1 e 10, que escolhi')
    número_random = random.randint(0, 10)
    limite_tentativas = 5
    pontuação_maxima = 100
    pontuação_minima = 10
    for tentativas in range(1, limite_tentativas + 1):
        while True:
            try:
                chute = int(input(f'Digite seu palpite: '))
                if chute < 1 or chute > 10:
                    print (f'Valor inválido. Digite um número entre 1 e 10. ')
                    continue
                break
            except ValueError:
                print (f'Valor inválido. Digite um número entre 1 e 10. ')
        if chute == número_random:
            pontuação = pontuação_minima + (pontuação_maxima - pontuação_minima) * (limite_tentativas - tentativas) / (limite_tentativas - 1)
            print (f'Parabéns, você acertou o número escolhido, que foi o {número_random}')
            print (f'Sua pontuação foi {pontuação}')
            break
        else:
            print (f'Ainda não! Você está na tentativa {tentativas}')

    else: 
        print(f'Que pena, você não conseguiu acertar e portanto, não pontuou!')

def iniciar_nova ():
    while True:
        tentativa ()
        resposta = input(f'Você gostaria de jogar novamente? Digite sim ou não: ')
        if resposta.lower() != "sim":
            print (f'Obrigado por jogar, até a próxima.')
            break


iniciar_nova ()






    