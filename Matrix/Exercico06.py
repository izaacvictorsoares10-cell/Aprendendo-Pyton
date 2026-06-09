print("-------------------------------------------")
print("Bem vindo ao campo de BATALHA NAVAL 4x4")
print("-------------------------------------------")

print("Voce tem que acertar o meu Navil, mas voce tem que acha-lo primeiro!!")
print("Escolha uma posicao de 1 a 4 para tentar acertar com seu BARRIL")

oceano = [
        ["N" , "~" , "~" , "~"],
        ["~" , "~" , "~" , "~"],
        ["~" , "~" , "~" , "~"],
        ["~" , "~" , "~" , "~"] ]

while True:
    linha,coluna = input("Escolha a linha e a coluna que voce quer lancar seu BARRIL, separado por virgula: ").split(",")
    if oceano [int(linha)-1][int(coluna)-1]== "N":
        print("BARRILLLLL, vc afundou meu navil!")
        break
    print("Nao acertou seu BARRILL, tente novamente: ")

