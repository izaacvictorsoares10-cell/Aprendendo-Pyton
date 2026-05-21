frequencia = int(input("Informe quantas aulas foi: "))
if frequencia > 0 :
    nota1= float(input("Nota final dia 1: ").replace("," , "."))
    nota2= float(input("Nota final dia 2: ").replace("," , "."))
    media= (nota1 + nota2) / 2
    if media >= 7 :
        print("Aprovado") 
    elif media >= 5 : 
        print("Fazer recuperacao")
        notRec= float(input("Nota da Recuperacao : ").replace("," , "."))
        if notRec  >= 6 : 
            print("Aprovado com Recuperacao")  
        else :  
            print("Reprovado")
    else : 
        print("Panguou")        
else:
    print("Falto calotero")
      