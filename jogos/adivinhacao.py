import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        tentativa_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , tentativa_str)
        tentativa = int(tentativa_str)

        if(tentativa < 1 or tentativa > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = tentativa == numero_secreto
        maior   = tentativa > numero_secreto
        menor   = tentativa < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu tentativa foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu tentativa foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - tentativa)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
