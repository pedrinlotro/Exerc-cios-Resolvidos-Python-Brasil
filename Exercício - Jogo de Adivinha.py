import random

def tentativa ():
    print (f'Bem vindo ao jogo! Você deve adivinhar qual número, entre 1 e 10, que escolhi')
    número_random = random.randint(0, 10)
    tentativas = 5
    for tentativas in range(1, tentativas + 1):
        chute = int(input(f'Digite seu palpite: '))
        if chute == número_random:
            print (f'Parabéns, você acertou o número escolhido, que foi o {número_random}')
            break
        else:
            print (f'Ainda não! Você está na tentativa {tentativas}')

    else: 
        print(f'Que pena, você não conseguiu acertar!')

tentativa ()








    