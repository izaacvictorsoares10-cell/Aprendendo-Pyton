import time

while True:
    usuario = input('Digite o Usuario: ').upper()
    match usuario :
        case 'ADMIN':
            print('Acesso total: Criar, Ler, Atualizar e Deletar')
        case 'GERENTE':
            print('Acesso gerencial: Criar, Ler e Atualizar.')
        case 'EDITOR':
            print('Acesso de conteúdo: Ler e Atualizar.')
        case 'VISITANTE':
            print('Acesso para Ler e observar.')
        case _ :
            hacker = input("Voce e um hacker? (S/N): ")[0].lower()
            while hacker == "s":
                tempo = 5
                while tempo > 0:
                        time.sleep(1)
                        print(tempo)
                        tempo -= 1
                        if tempo == 0:
                            print('Vai exploder!!')
                            hacker = "N"
            if hacker == "N" :
                break