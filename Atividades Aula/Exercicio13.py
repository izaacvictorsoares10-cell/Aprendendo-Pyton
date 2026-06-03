carrinho = []
continuar = "continuar"
while continuar == "continuar".lower():
    listaDeCompras = input("O que voce quer colocar na sua lista? ")
    if listaDeCompras == "sair":
        break

    carrinho.append(listaDeCompras)
    carrinho.sort()

print(carrinho)