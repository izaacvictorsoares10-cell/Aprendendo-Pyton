produtos = {"monster": 10,
            "doritos 200kg": 20,
            "creatina": 100
           }

produtosPegos = input("Quer iniciar sua compra: (s/n) ").lower()[0]
while produtosPegos == "s":
    carrinho = input("Qual produto voce quer? ")
    print(produtos.get(carrinho, "valor nao encontrado!"))
    continuar = input("Vai continuar? (s/n) ").lower()[0]
    if produtosPegos == "n":
        print("Agradecemos pela escolha!")
        break
