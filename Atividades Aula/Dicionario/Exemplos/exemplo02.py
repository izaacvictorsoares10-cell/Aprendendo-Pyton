dados_pessoais = {
    "nome": "Joao",
    "idade": 21,
    "nascimento": "20/05/2005",
    "sexo": "M",
    "altura": 1.70,
    "tem CNH": True }

for chave,valor in dados_pessoais.items():
    print(f"{chave}:{valor}")