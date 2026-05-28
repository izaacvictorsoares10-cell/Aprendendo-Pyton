nota = float(input("Digite um Numero de 0 a 10: "))
while nota < 0 or nota > 10:
        nota = float(input("Valor invalido!\nInsira a nota novamente: "))
print("Nota valida")