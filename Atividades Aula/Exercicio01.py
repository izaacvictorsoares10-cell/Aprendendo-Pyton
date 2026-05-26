numerosLista = []

for i in range(6):
    numero = int(input(f"Digite o {i + 1}° numero: "))
    numerosLista.append(numero)

numerosLista.sort()
print(numerosLista)
soma = sum(numerosLista)
print(f"A soma dos numeros e = {soma}")
print("O maior numero e =",(max(numerosLista)))
print("O menor numero e =" ,(min(numerosLista)))


