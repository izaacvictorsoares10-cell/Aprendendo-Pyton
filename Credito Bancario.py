salario = float(input("Qual seu salario? ").replace("," , "."))
parcela = float(input("Qual sua Parcela? ").replace("," , "."))

x = salario * 30 / 100
if parcela > x :
    print("Credito Recusado")
else:
    print("Credito Aprovado")