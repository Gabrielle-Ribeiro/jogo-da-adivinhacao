import random

def jogar():
    print("**************************")
    print("Bem vindo ao Jogo de Forca")
    print("**************************")
    print("")

    palavras = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        print(letras_acertadas)

        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute.upper() == letra.upper():
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()