listaEmails = ["joao@gmail.com", "maria@senac.df", "pedro@outlook.com", "ana@senac.df"]
emailsSenac = []

for email in listaEmails:
    if "@senac.df" in email:
        emailsSenac.append(email)
print(*emailsSenac)

