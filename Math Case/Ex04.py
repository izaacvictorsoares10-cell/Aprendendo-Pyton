while True:

    cod = int(input('Digite o codigo do Produto: '))
    match cod:
        case 100 :
            print('Cachorro-Quente - R$ 10,00')
        case 101:
            print('Bauru Simples - R$ 12,00')
        case 102:
            print('X-Salada - R$ 15,00')
        case 103:
            print('Hamburguer - R$ 13,00')
        case _ :
            print('Codigo de Produto Invalido!')
