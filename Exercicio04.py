nasc = int(input("Qual o ano do seu nascimento? "))

idade = 2026 - nasc
if idade > 60 :
    print("Voce e veio")
elif idade < 18 :
    print("babao")
else :
    print("jovem adulto")