from unittest import result

while True:
    opcao = input("1-Somar\n2-Subtrair\n3-Multiplicar\n4-Dividir\n5-Sair\nEscolha a Opcao:\n")
    if opcao == 1:
     nume1 = float(input("Digite o 1° numero:"))
     nume2 = float(input("Digite o 2° numero:"))
     resultado = nume1 + nume2