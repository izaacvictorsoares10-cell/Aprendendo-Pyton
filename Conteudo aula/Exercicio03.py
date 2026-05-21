nume1 = int(input("digite primeiro numero: ").replace ("." , ","))
nume2 = int(input("digite o segundo numero: ").replace("." , ","))

if nume1 > nume2 :
    print("O primeiro numero e menor")
elif nume2 > nume1 :
    print("O segundo numero e maior")
else :
    print("Os dois sao enguais")


