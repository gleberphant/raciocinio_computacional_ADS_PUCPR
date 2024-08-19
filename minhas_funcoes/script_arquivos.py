""" scripts de manipulação de arquivos"""
# """ scripts de manipulação de arquivos"""
# Curso: Análise e Desenvolvimento de Sistemas
# Aluno: Handerson Gleber de Lima Cavalcanti (Gr4v4t1nh4)
#
#

import pickle


ARQUIVO_PATH = "minhas_funcoes\\dados.data"

dados = {
    "nome": "joão",
    "idade": 25,
    "cidade": "curitiba",
    "frutas_favoritas": [
        "maça",
        "banana",
        "laranja"
    ]
}

lista_de_dados = [dados] * 3

with open(ARQUIVO_PATH, "wb") as file1:
    pickle.dump(lista_de_dados, file1)


with open(ARQUIVO_PATH, "rb") as file2:
    resultado = pickle.load(file2)

for objeto in resultado:
    print("objeto ", type(objeto))
    for k, v in objeto.items():
        print("| Key: ", k, end=': ')
        if isinstance(v, list):
            print("", end='')
            for vv in v:
                print(vv, end=' ')
        else:
            print("", v, end='')
        print("")

# with open("pessoa.json", "r", encoding="utf-8") as arquivo_leitura:
#     dados_lidos = json.load(arquivo_leitura)

# for k, v in dados_lidos.items():
#     print(f"│ {str(k):<20} : {str(v):<25}   │")
# # tupla = ("elemento1",
# #          "elemento2",
# #          "elemento3")
#
# dicionario = {"cod": "001",
#               "nome": "teste01"}
#
#
# with open("jason\\jason_teste.json", "w", encoding="utf-8") as arquivo:
#     # comentario para explicar tudo
#     arquivo.write(str(dicionario) + "\n")
#     arquivo.write(str(dicionario) + "\n")
# #   arquivo.write(str(tupla) + "\n")
#
#
# # with open("jason\\jason_teste.json", "r", encoding="utf-8") as arquivo:
# #     linhas = arquivo.readlines()
# #     print(f"##################################################")
# #     print(f"# {'codigo':<10} | {'nome':<10} | {'tipo':<20} #")
# #     for linha in linhas:
# #         objeto = eval(linha)
# #         print(f"# {objeto['cod']: <10} | {objeto['nome']: <10} | {str(type(objeto)):<20} #")
# #     print(f"##################################################")
# #     arquivo.close()
