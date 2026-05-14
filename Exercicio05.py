numeP = float(input("Qual seu peso: ").replace("," , "."))
numeA = float(input("Qual sua Altura: ").replace("," , "."))

imc = numeP / (numeA ** 2)
print("Seu imc e :", imc)