listaMaior = []
listaMenor = []#vetor

for n in range(7):
    nascimento = int(input("Data de nascimento: "))
    idade = 2026 - nascimento
    if idade >= 18 :
        listaMaior.append(idade)
    else :
        listaMenor.append(idade)

print(f"Os maiores de idade sao: {listaMaior} e a quantidade deles sao: {len(listaMaior)}")
print(f"Os menores de idade sao: {listaMenor} e a quantidade deles sao: {len(listaMenor)}")