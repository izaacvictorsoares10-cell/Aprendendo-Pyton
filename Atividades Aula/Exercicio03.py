listaPrincipal = []
par = []
impar = []

for i in range(10):
    listaPrincipal.append(int(input(f"Digite o {i+1}ª numero:")))

for i in listaPrincipal:
    numero2 = i % 2
    if  numero2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f"os numeros impares sao: {impar}")
print(f"os numeros pares sao: {par}")
print(f"A lista e: {listaPrincipal}")