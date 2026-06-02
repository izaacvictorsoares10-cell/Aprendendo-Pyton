from unittest import result

while True:
    opcao = int(input("--------------\n1-Somar\n2-Subtrair\n3-Multiplicar\n4-Dividir\n5-Sair\n--------------\nEscolha a Opcao: "))
    if opcao == 5:
        print("saindo....")
        break
    if opcao == 1:
        nume1 = float(input("Digite o 1° numero:"))
        nume2 = float(input("Digite o 2° numero:"))
        print(f"O resultado da soma e : {nume1 + nume2}")
    if opcao == 2:
        nume1 = float(input("Digite o 1° numero: "))
        nume2 = float(input("Digite o 2° numero: "))
        print(f"O resultado da subtrair e : {nume1 - nume2}")
    if opcao == 3:
        nume1 = float(input("Digite o 1° numero: "))
        nume2 = float(input("Digite o 2° numero: "))
        print(f'O resultado da multiplicao e : {nume1 * nume2}')
    if opcao == 4:
        nume1 = float(input('Digite o 1° numero: '))
        nume2 = float(input('digite o 2° numero: '))
        print(f'O resultado da divisao e : {nume1 / nume2}')