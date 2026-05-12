
n1 = int(input ("digite o primeiro numero: "))
n2 = int(input("digite o segundo numero: "))



resultado = n1 // n2
resultado2 = n1 % n2
resultado3 = n1 ** n2

print("O resultado da parte inteira da divisao e :", resultado)
print("O resultado2 do resto da divisao e : :", resultado2)
print("O resultado da potencia e : ", resultado3)


print("------------------------------------------------")
print("   OPERADOR RELACIONAIS       ")
print("------------------------------------------------")\


relacao1 = n1 > n2
relacao2 = n1 < n2
relacao3 = n1 >= n2
relacao4 = n1 <= n2
relacao5 = n1 == n2
relacao6 = n1 != n2

print("Os resultados das relacao estarao abaixo \n{} \n{} \n{} \n{} \n{} \n{}" .format(relacao1, relacao2, relacao3, relacao4, relacao5, relacao6))