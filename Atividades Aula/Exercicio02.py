notas= []
for i in range(4):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)
media = sum(notas) / len(notas)
if media >= 7.0:
    print(f"Notas: {notas}")
    print("Aprovado")
else:
    print("Recuperação")