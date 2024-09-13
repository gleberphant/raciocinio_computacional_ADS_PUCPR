""" sitema de gestão academica - pucpr VS6"""
# ┌─────────────────────────────────────────────────────────────┐
# │         ╔════╗           ╔═════     ╔════╗  ╔═══╗           │
# │         ║    ║  ║    ║   ║          ║    ║  ║   ║           │
# │         ╠════╝  ║    ║   ║          ╠════╝  ╠═══╩╗          │
# │         ║       ╚════╝   ╚═════     ║       ║    ║          │
# └─────────────────────────────────────────────────────────────┘
# ┌─────────────────────────────────────────────────────────────┐
# │  CURSO: Análise e Desenvolvimento de Sistemas               │
# │  DISCIPLINA: Raciocínio Computacional (11100010563_20242_02)│
# │  ALUNO: HANDERSON GLEBER DE LIMA CAVALCANTI (Gr4v4t1nh4)    │
# │  MATRÍCULA: 1112024201103                                   │
# └─────────────────────────────────────────────────────────────┘
# ┌─────────────────────────────────────────────────────────────┐
# │   Atividade FORMATIVA 5 - semana 7                          │
# └─────────────────────────────────────────────────────────────┘
# CRITÉRIOS
# -	Função para salvar lista de estudantes em um arquivo JSON.
# -	Função para recuperar lista de estudantes de um arquivo JSON e armazenar em uma variável em memória.
# -	Adaptação das funções de incluir, listar, excluir e editar estudantes para que acessem as duas funções acima sempre
# que necessário.
import json
import os


# Função para salvar dados em um arquivo json
# recebe o dicionário com os dados e um nome da base destino.
# Retorna true se tudo certo.


def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def salvar_em_arquivo(dados_param, nome_arquivo_destino_param="itens"):

    print("salvando dados de ", nome_arquivo_destino_param, " ... ", end=' ')

    try:
        with open("jayzon_" + nome_arquivo_destino_param + ".json", "w", encoding='utf8') as arquivo_escrita:
            json.dump(dados_param, arquivo_escrita, ensure_ascii=False)
            print("Dados salvo com sucesso ")

    except Exception as erro:
        print(f"***** Erro inesperado  :{erro} **** \n  ")
        print(f"***** os dados não foram salvos **** \n  ")

    return True

# função para abrir arquivo json
# recebe o nome da base de dados
# retorna lista com os dados


def abrir_arquivo(nome_base_destino_param="itens"):
    """ Função para abrir o arquivo de dados e retorna uma lista """

    print(" [ Abrindo arquivo : ", nome_base_destino_param, " ... ] ", end='\n')

    try:
        with open("jayzon_" + nome_base_destino_param + ".json", "r", encoding='utf8') as arquivo_leitura:
            data_return = json.load(arquivo_leitura)
    except Exception as erro:
        print(f"***** Erro inesperado  :{erro} **** \n  ")
        print("[ Carregando dados de teste .... ]")
        data_return = popula_dados_teste()

    return data_return


#  Esta funcao desenha o menu principal da aplicação. Coloquei em uma função para não poluir o código principal
def mostra_menu_principal():
    """

    Returns:

    """
    limpar_tela()
    print("")
    print("┌───────────────[ MENU PRINCIPAL ]──────────────┐")
    print("│                                               │")
    print("│ (1) Gerenciar Estudantes.                     │")
    print("│ (2) Gerenciar Professores.                    │")
    print("│ (3) Gerenciar Disciplinas.                    │")
    print("│ (4) Gerenciar Turmas.                         │")
    print("│ (5) Gerenciar Matrícula.                      │")
    print("│                                               │")
    print("│ (9) Sair.                                     │")
    print("│                                               │")
    print("└───────────────────────────────────────────────┘")
    return None


# Esta funcao desenha o menu secundário da aplicação. Coloquei em uma função para não poluir o código principal
# ela recebe como parametro o menu secundário que é para ser desenhado. Tendo como valor padrão o menu ESTUDANTE
def mostra_submenu():
    limpar_tela()
    print("")
    print("┌──────────────[ MENU OPERAÇÕES ]───────────────┐")
    print("│                                               │")
    print("│ (1) Incluir.                                  │")
    print("│ (2) Listar.                                   │")
    print("│ (3) Atualizar.                                │")
    print("│ (4) Excluir.                                  │")
    print("│                                               │")
    print("│ (9) Voltar                                    │")
    print("│                                               │")
    print("└───────────────────────────────────────────────┘")
    return None


# Esta funcao desenha a mensagem de opção inválida. Coloquei em uma função para não poluir o código principal
def msg_opcao_invalida():
    print("\t╔════════════════════╗")
    print("\t║   OPÇÃO INVÁLIDA   ║")
    print("\t╚════════════════════╝")
    return None


# Esta funcao desenha a mensagem de saida da aplicação. Coloquei em uma função para não poluir o código principal
def msg_saida():
    limpar_tela()
    print("")
    print(" ╔════════════════════════════════════════════╗")
    print(" ║      Dúvidas e sugestões?                  ║")
    print(" ║      Entre em contato por                  ║")
    print(" ║      handerson.gleber@gmail.com            ║")
    print(" ╚════════════════════════════════════════════╝")
    return None


# Esta funcao desenha a mensagem de abertura da aplicação. Coloquei em uma função para não poluir o código principal
def msg_abertura():
    limpar_tela()
    print("")
    print(" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print(" ░░░░░░░░░░SISTEMA DE GESTÃO ACADÊMICA░░░░░░░░")
    print(" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print(" ░░░░ por: HANDERSON GLEBER (gravatinha) ░░░░░")
    print(" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("")
    msg_enter_continua()
    return None


def msg_enter_continua():
    input("\t Pressione <ENTER> para continuar ...")
    return None


def popula_dados_teste():
    lista = []
    for i in range(8):
        lista.append({"codigo": 1 * i, "nome": "aluno_" + str(i), "cpf": str(i) * 6})
    return lista


def inserir_item(novo_item, lista_param):

    lista_param.append(novo_item)
    print(f"\t Item inserido com sucesso: \n \t {1} ", novo_item['nome'])

    return lista_param


def listar_itens(lista_param, nome="ITENS"):
    limpar_tela()
    print("")
    print("┌───────────────────────────────────────────────┐")
    print("│            LISTAR {0:<11}                 │".format(nome))
    print("│                                               │")
    if len(lista_param) > 0:
        k = list(lista_param[0].keys())

        print("├────────┬─────────────────────────┬────────────┤")
        print(f"│ {k[0]:<6} │ {k[1]:<23} │ {k[2]:<11}│")  # desenha o cabeçalho (keys) da tabela

        for item in lista_param:  # desenha cada linha da tabela
            print("├────────┼─────────────────────────┼────────────┤")
            print(f"│ {item[k[0]]:<6} │ {item[k[1]]:<23} │ {item[k[2]]:<11}│")
        print("└────────┴─────────────────────────┴────────────┘")
        print("")
    else:
        print("│                                               │")
        print("│        *** Não há item cadastrado ***         │")
        print("│                                               │")
        print("└───────────────────────────────────────────────┘")
    return None


def buscar_item(lista_param):

    # filtro de entrada - laço obriga usuário digitar um número
    while True:
        codigo_busca = input("\n Digite o Codigo do item buscado: ")

        if codigo_busca.isdigit():
            break
        else:
            print("*** código inválido. **** ")
            print("*** Digite um código númérico. **** ")

    # varre a lista em busca do item procurado
    for index, item in enumerate(lista_param):
        if int(codigo_busca) == item['codigo']:  # procura item com o código informado
            return index  # retorna o item encontrado
    else:
        print("\t╔══════════════════════════╗")
        print("\t║   Item não encontrado    ║")
        print("\t╚══════════════════════════╝")
        input(" pressione <ENTER> para continuar")

    return False


def remover_item(lista_param):
    item_index = buscar_item(lista_param)

    if item_index is not False:
        item_encontrado = lista_param[item_index]['nome']
        print("\t╔════════════════════════════════════════════════════════════╗")
        print(f"\t║    tem certeza que deseja excluir {item_encontrado:^20} ?   ║")
        print("\t╚════════════════════════════════════════════════════════════╝")
        while True:

            confirmacao = input("\t Digite [S] para SIM  ou [N] para NÃO ").upper()

            # Resposta SIM - deletar o aluno
            if confirmacao == "S":
                try:
                    del lista_param[item_index]
                except Exception as erro:
                    print("*** falha na exclusao *** \n Erro :", erro)
                else:
                    print("\t╔═══════════════════════════════════════════╗")
                    print("\t║ ****    ITEM EXCLUIDO COM SUCESSO    **** ║")
                    print("\t╚═══════════════════════════════════════════╝")
                finally:  # em qualquer caso quebra o laço while de confirmação da exclusão
                    break

            # resposta NÃO - cancelar exclusão
            elif confirmacao == "N":
                print("\t╔════════════════════════╗")
                print("\t║   EXCLUSÃO CANCELADA   ║")
                print("\t╚════════════════════════╝")
                break  # quebra o laço while de confirmação da exclusão
                # resposta inválida
            else:
                print("\t╔════════════════════╗")
                print("\t║   OPÇÃO INVÁLIDA   ║")
                print("\t╚════════════════════╝")

    return lista_param


def editar_item(lista_param):

    item_index = buscar_item(lista_param)

    if item_index is not False:
        novo_item = {'codigo': lista_param[item_index]['codigo'],
                     'nome': input("\n Digite o novo nome: "),
                     'cpf': input("\n Digite o novo CPF: ")}

        try:  # tenta atualizar o aluno
            lista_param[item_index] = novo_item

        except Exception as erro:  # se ocorrer um erro
            print(" *** ocorreu um erro quando estava atualizando o aluno **** \n Erro = ", erro)

        else:  # se funcionar
            print("\t╔═══════════════════════════════════════════╗")
            print(f"\t║ *** ALUNO {novo_item['codigo']:<4} ATUALIZADO COM SUCESSO *** ║")
            print("\t╚═══════════════════════════════════════════╝")

    return lista_param


def main():

    lista_alunos = abrir_arquivo()

    gerador_codigo_aluno = lista_alunos[len(lista_alunos)-1]['codigo'] + 1

    msg_abertura()  # chama mensagem de abertura da aplicação

    while True:  # Loop principal da aplicação. Roda enquanto não receber um BREAK

        mostra_menu_principal()  # chama o desenho do menu principal

        opcao_menu_principal = input("\t Informe o numero da opção desejada:  ")[0]

        if opcao_menu_principal == "1":  # ENTRA NO MENU DE ESTUDANTE

            while True:  # Loop no menu secundário. Roda enquanto não receber um BREAK

                mostra_submenu()

                opcao_submenu1 = input("\t Informe o número da opção desejada: ")

                match opcao_submenu1:
                    case "1":  # Opção de INCLUIR

                        novo_item = {"codigo": gerador_codigo_aluno, "nome": input("\t Informe o NOME a ser inserido:  "),
                                     "cpf": input("\t Informe o CPF a ser inserido:  ")}

                        lista_alunos = inserir_item(novo_item, lista_alunos)

                        salvar_em_arquivo(lista_alunos)

                        gerador_codigo_aluno += 1
                        msg_enter_continua()

                    case "2":  # Opção de LISTAR
                        print("\t RELAÇÃO DOS ALUNOS CADASTRADOS")

                        listar_itens(lista_alunos)

                        msg_enter_continua()

                    case "3":  # Opção de EDITAR

                        lista_alunos = editar_item(lista_alunos)
                        salvar_em_arquivo(lista_alunos)
                        msg_enter_continua()

                    case "4":  # Opção de EXCLUIR

                        lista_alunos = remover_item(lista_alunos)
                        salvar_em_arquivo(lista_alunos)
                        msg_enter_continua()

                    case "9" | "q":  # Opção de SAIR
                        print("Voltando ao menu principal")
                        break

                    case _:  # CASO O USUÁRIO DIGITE OPÇÃO INVALIDA
                        msg_opcao_invalida()

        elif (opcao_menu_principal == "2"
              or opcao_menu_principal == "3"
              or opcao_menu_principal == "4"
              or opcao_menu_principal == "5"):  # OUTROS MODULOS DO MENU PRINCIPAL

            print("")
            print(" ╔════════════════════════════════════════════╗")
            print(" ║            EM DESENVOLVIMENTO              ║")
            print(" ╚════════════════════════════════════════════╝")
            print("")
            msg_enter_continua()

        elif opcao_menu_principal == "9" or opcao_menu_principal == "q":  # OPÇÃO SAIR DO MENU PRINCIPAL
            msg_saida()
            salvar_em_arquivo(lista_alunos)
            return None
        else:  # CASO O USUÁRIO DIGITE OPÇÃO INVALIDA
            msg_opcao_invalida()


if __name__ == "__main__":

    print("Iniciando o programa... ")
    main()
    print("Programa finalizado... ")
    exit(0)
