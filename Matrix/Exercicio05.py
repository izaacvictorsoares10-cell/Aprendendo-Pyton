vendas = [
    [1200, 850, 900, 1500],
    [900, 1100, 1000, 1300],
    [1500, 1600, 1400, 1800],
    [700, 600, 800, 900]]

vendas_vendedores = []
for vendedor in vendas:
    total_vendas = 0
    for total_dia in vendedor:
        total_vendas += total_dia
    vendas_vendedores.append(total_vendas)

print(f"""Total de vendas por vendedores e =
R${vendas_vendedores[0]:.2f}
R${vendas_vendedores[1]:.2f}
R${vendas_vendedores[2]:.2f}
R${vendas_vendedores[3]:.2f}
""")

vendas_dias = [0, 0, 0, 0]
for vendedor in range(len(vendas)):
    for dia in  range(len(vendas[0])):
        vendas_dias[dia] += vendas[vendedor][dia]
print("total de vendas por dia: ")
for i in range(len(vendas)):
    print(f"Dia {i+1} = R$ {vendas_dias[i]:.2f}")