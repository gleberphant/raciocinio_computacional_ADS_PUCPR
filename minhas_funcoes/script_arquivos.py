""" scripts de manipulação de arquivos"""
# """ scripts de manipulação de arquivos"""
# Curso: Análise e Desenvolvimento de Sistemas
# Aluno: Handerson Gleber de Lima Cavalcanti (Gr4v4t1nh4)
#
tupla = ("elemento1",
         "elemento2",
         "elemento3")

dicionario = {"cod": "001",
              "nome": "teste01"}


with open("jason\\jason_teste.json", "w", encoding="utf-8") as arquivo:
    # comentario para explicar tudo
    arquivo.write(str(dicionario) + "\n")
    arquivo.write(str(dicionario) + "\n")
#   arquivo.write(str(tupla) + "\n")


with open("jason\\jason_teste.json", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    print(f"##################################################")
    print(f"# {'codigo':<10} | {'nome':<10} | {'tipo':<20} #")
    for linha in linhas:
        objeto = eval(linha)
        print(f"# {objeto['cod']: <10} | {objeto['nome']: <10} | {str(type(objeto)):<20} #")
    print(f"##################################################")
    arquivo.close()
