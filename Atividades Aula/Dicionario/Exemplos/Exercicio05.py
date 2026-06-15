palavras = {}
frase = input("Digite uma palavra: ").split()
for n in frase:
    if n not in palavras:
        palavras[n] = 1
    else:
        palavras[n] += 1
print(palavras)