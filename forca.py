def jogar():
    print("**************************")
    print("Bem vindo ao Jogo de Forca")
    print("**************************")
    print("")

    palavra_secreta = "python"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        print(letras_acertadas)

        chute = input("Qual a letra? ")

        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()