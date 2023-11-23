def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "bergamota".lower()
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    # enquanto não enforcou e não acertou
    while ((not enforcou) and (not acertou)):

        tentativa = input("Qual letra? ")
        tentativa = tentativa.strip().lower()

        if (tentativa in palavra_secreta):
            for index, letra in enumerate(palavra_secreta):
                if (tentativa == letra):
                    letras_acertadas[index] = letra
        else:
            erros += 1
        enforcou = (erros == 6)
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
