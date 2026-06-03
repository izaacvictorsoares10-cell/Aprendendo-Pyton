maior18 = []
listaHomi = []
femeaMenor = []
continuar = "S"

while continuar == "S":
    idade = int(input('Digite sua idade: '))
    sexo = input('Diga seu sexo: (M/F) ').upper()[0]

    if idade >18:
        maior18.append(idade)
    if sexo == "m":
        listaHomi.append(sexo)
    if sexo == "f" and idade <20:
        femeaMenor.append(sexo + str(idade))

    continuar = input("Deseja continuar os cadastros? ").upper()[0]

print(f"Essa e a quantidade de cadastros com mais de 18 anos : {len(maior18)}")
print(f"Esse foi o total de pessoas cadastradas do genero masculino: {len(listaHomi)}")
print(f"Essa e a quantidade de pessoas do genero feminino e menorers de 20 anos cadastradas: {len(femeaMenor)}")
