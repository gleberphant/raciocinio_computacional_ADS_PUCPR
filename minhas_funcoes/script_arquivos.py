""" scripts de manipulação de arquivos"""
# """ scripts de manipulação de arquivos"""
# Curso: Análise e Desenvolvimento de Sistemas
# Aluno: Handerson Gleber de Lima Cavalcanti (Gr4v4t1nh4)
#


with open("jason\\jason_teste.json", "w", encoding="utf-8") as arquivo:
    # comentario para explicar tudo
    arquivo.write("nesse eh  um arquivi")
    arquivo.write("\njason = {'nome':'nome1', 'cpf':'123'}")

with open("jason\\jason_teste.json", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    for linha in linhas:
        print(">> " + linha)
