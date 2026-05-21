lado1 = float(input("Qual a medida do primeiro lado? ").replace("," , "."))
lado2 = float(input("a do segundo? ").replace("," , "."))
lado3 = float(input("a do terceiro? ").replace("," , "."))

if lado1+lado2<lado3 or lado1+lado3<lado2 or lado2+lado3<lado1:
    print("esse triangulo nao existe")
else:
    if lado1==lado2==lado3 :
        print("Esse triangulo e equilatero")
    elif lado1==lado2!=lado3 or lado1==lado3!=lado2 or lado2==lado3!=lado1:
        print("esse triangulo e isoseles")
    elif lado1!=lado2!=lado3 :
        print("esse triangulo e escaleno")