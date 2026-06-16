estoque = {"Teclado": 15, "Mouse": 22, "Monitor": 8}
selecao = {}
print(estoque)
atualiza_estoque = False
continuar = "s"
while continuar == "s":
    nome, quantidade = input("Digite o nome do item e a quantidade que deseja separados por virgula: ").split(",")
    retorno = estoque.get(nome, "Produto nao encontrado!")
    for chave, valor in estoque.items():
        if nome.lower() == chave.lower():
            if valor == 0 :
                print("Estoque esgotado!")
                continue
            if valor < int(quantidade):
                print("Estoque Insuficiente!")
                continue
            else:
                estoque[chave] -= int(quantidade)

                atualiza_estoque = True
    if atualiza_estoque:
        print("Estoque Atualizado")
        for chave, valor in estoque.items():
            print(f"{chave} : {valor}")