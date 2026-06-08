matriz_base = [[1, 2], [3, 4]]
fator = int(input("Digite um numero para a multiplicacao da matriz: "))
multiplicacao = []
for i in matriz_base:
    matriz_linha = []
    for j in i:
        matriz_linha.append(j*fator)
    multiplicacao.append(matriz_linha)
print(multiplicacao)