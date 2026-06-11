quadrados = {}
for i in range(1, 6):
    quadrados.setdefault(i, i**2)
    #print(quadrados)
for k,v in quadrados.items():
    print(f"{k} -> {v}")