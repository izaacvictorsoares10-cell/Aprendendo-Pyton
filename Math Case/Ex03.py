while True:
    notas = input('Digite o conceito do aluno: ').upper()
    match notas:
        case 'A':
            print("Brabo Demais Disgrama!")
        case 'B':
            print("Mando bem menozin!")
        case 'C':
            print("Satisfação meno!")
        case 'D':
            print("Abre os Zoio menor!")
        case 'F':
            print("Reprovo Menorzin, estriguinou disgrama!")
        case _ :
            print("Ta chapando, isso existe não!")
