dados_pessoais = { "Nome": "Izaac",
                   "Idade": 20,
                   "Ama a Namorada": True,
                   "Ama Hollow Knight": "Sim"
                   }

dados_profissionais = {"Trampo": "Garoto de programa",
                       "Lugar": "SENAC",
                       "salario": 69696969,
                       "Carro": "Opalao",
                       "horario": "4hrs"
                       }
perfil_completo = dados_pessoais|dados_profissionais
for k,v in perfil_completo.items():
    print(f"{k} : {v}")