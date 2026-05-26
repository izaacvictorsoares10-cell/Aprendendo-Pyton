senha = "senha"

for s in range(1,4):
    senhaPessoal = input(f"Digite a senha, esta e a sua {s}° tentativa: ")
    if senhaPessoal == senha :
        print("Acesso Permitido!")
        break
    elif senhaPessoal != senha :
        print("Acesso negado!"),[3]

else:
    print("Conta Bloqueada")
