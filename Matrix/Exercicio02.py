estoque = [[12, 5, 8],
           [3, 15, 2],
           [19, 0, 7]]

prateleira,divisoria = input("Digite a prateleira e a coluna para acessar seu produto: ").split(",")
#prateleira = int(prateleira)-1
#divisoria = int(divisoria)-1
print(estoque[int(prateleira)-1][int(divisoria)-1])