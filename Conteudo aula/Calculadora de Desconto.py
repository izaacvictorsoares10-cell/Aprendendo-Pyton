valorCompras = float(input("Valor final da compra: ").replace("," , "."))

if valorCompras <= 100:
    print(f"Voce nao teve desconto. O valor total da sua compra e de {valorCompras}")
elif valorCompras > 100 and valorCompras < 300 :
    valorDesconto = valorCompras * 0.05
    valorComDesconto = valorCompras - valorDesconto
    print(f"Voce teve um desconto de 5% no valor de {valorDesconto}. Sua compra ficou um valor total de : {valorComDesconto}")
elif valorCompras > 300 and valorCompras < 500:
    print(f"Voce teve um desconto de 10% no valor de {valorCompras*0.1}. Sua compra ficou um valor total de : {valorCompras*0.9}")
elif valorCompras >500 :
    valorCompras = valorCompras * 0.15
    print(f"Voce teve um desconto de 15% no valor de {valorCompras
    }. Sua compra ficou um valor total de : {valorCompras}")