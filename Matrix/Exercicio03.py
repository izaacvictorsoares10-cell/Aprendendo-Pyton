matriz_quadrada = [
        [5, 2, 9],
        [1, 8, 3],
        [4, 7, 19]]
somaMatriz = 0
numeros =[]
for i in range(len(matriz_quadrada)):
    numeros.append(str(matriz_quadrada[i][i]))
    somaMatriz += matriz_quadrada[i][i]
print(f"A soma da diagonal da matriz quadrada de {" + ".join(numeros)} = {somaMatriz}")



# O resultado esperado deve ser: 5 + 8 + 6 = 19