while True:
    mes = input('Digite o mes ou o numero do mes: ')
    match mes.lower():
        case "janeiro" | "fevereiro" | "dezembro" | '1' | '2' | '12' :
            print("A estacao desse mes e inverno.")
        case "marco" | "abril" | "maio" | '3' | '4' | '5':
            print("A estacao desse mes e Primavera.")
        case "junho" | "julho" | "agosto" | '6' | '7' | '8':
            print("A estacao desse mes e Verao.")
        case 'setembro' | "outubro" | "novembro" | '9' | '10' | '11':
            print("A estacao desse mes e Outono.")
        case _ :
            print('Digite um Mes Valido!')