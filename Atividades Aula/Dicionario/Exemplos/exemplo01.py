dados_pessoais = {
    "nome": "Joao",
    "idade": 21,
    "nascimento": "20/05/2005",
    "sexo": "M",
    "altura": 1.70,
    "tem CNH": True }

print(dados_pessoais.keys())#chave tem quer unica

continuar = "s"
while continuar == "s":
    dados = input("Diga o dado que quer encontrar: ")
    print(dados_pessoais.get(dados, "Valor nao encontrado!"))
    continuar = input("Quer continuar? (s/n): ")[0].lower()
