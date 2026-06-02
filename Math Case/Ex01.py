while True:
    opcao = input('Digite uma letra ou saia com 0 : ').upper()

    match opcao:
        case "0":
            break
        case "A" | "E" | "I" | "O" | "U":
            print("Vogal")
        case _ :
            print("Consoante")
