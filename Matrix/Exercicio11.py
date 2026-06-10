matriz = [[5, 10],
          [3, 2]]
matriz_N = [n for con in matriz for n in con]
print(f"A soma de todos os numeros sao {sum(matriz_N)}")
