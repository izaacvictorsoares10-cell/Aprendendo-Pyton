import random
randomNum = random.randint(1, 20)
num = int(input("Advinhe meu Numero: "))
while num != randomNum :
    if num > randomNum :
        print("Seu numero e Maior que o meu!")
    else:
        print("Seu numero e menor que o meu! ")
    num = int(input("Voce errou, tente novamente: "))
print("Voce Acertou ze!!! Pabens!!!!!")