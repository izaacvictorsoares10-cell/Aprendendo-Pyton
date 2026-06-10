busca = [[1200, 850, 900, 1500], #vetor == lista
        [900, 1100, 1000, 1300],
        [1500, 1600, 1400, 1800]]
buscador = int(input("Procure seu numero na linha e na coluna: "))
achou = False

for i in range(len(busca)):
    for j in range(len(busca[i])):
        if busca [i][j]== buscador:
            print(f"O numero que voce procura esta na linha {i+1} e na coluna {j+1}.")
            achou = True
            break
    if achou :
        break
if not achou :
    print("numero nao encontrado.")