#nome = input("Olá, como você se chama? ")
#print("Bem-vindo ao jogo de adivinhação", nome, ". Você precisa acertar para encerrar o jogo. ")
#print("Tente adivinhar o número que estou pensando entre 1 e 20..")
#numero = 15
#if numero > 15:
#        print("Ta morno")
#else numero < 15:
#    print("Ta quente")
#palpite = int(input("Digite seu palpite"))

import random

nome = input("Olá, como você se chama? ")
print("Bem-vindo ao jogo de adivinhação", nome, ". Você precisa acertar para encerrar o jogo. ")
print("Tente adivinhar o número que estou pensando entre 1 e 20..")
numero = random.randint (1,20)
while True:
    palpite = int(input("Digite seu palpite: "))
    if palpite == numero:
        print("Acerto")
        break
    elif palpite > numero:
            print("Ta morno")
    else:
        print("Ta quente")
    
