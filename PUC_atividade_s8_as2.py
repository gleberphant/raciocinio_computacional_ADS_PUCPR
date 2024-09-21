""" Sistema de gestão academica - pucpr VS6"""
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
# -O que devo desenvolver?
# - Implementar todas as funcionalidades já desenvolvidas (ex.: incluir e listar) para os demais módulos do sistema.
# Veja os dados necessários para cada um dos grupos abaixo:
# Professores
# - Código do professor (Número inteiro)
# - Nome do professor (String)
# - CPF do professor (String)
#
# Disciplinas
# - Código da disciplina (Número inteiro)
# - Nome da disciplina (String)
#
# Turmas
# - Código da turma (Número inteiro)
# - Código do professor (Número inteiro)
# - Código da disciplina (Número inteiro)
#
# Matrículas
# - Código da turma (Número inteiro)
# - Código do estudante (Número inteiro)
#
# Validação de dados na manipulação de turmas e matrículas (verificar se um código já existe antes de incluir uma
# nova turma/matrícula com o mesmo código).
# - O que meu sistema deve ter no final? (checklist)
# - As quatro operações básicas (incluir/listar/atualizar/excluir) para todos os módulos
# (estudantes/professores/disciplinas/turmas/matrículas) do sistema.
# - Utilização de estruturas condicionais (if/elif/else) no código.
# - Utilização de estruturas de repetição (for ou while) para navegação dos menus
# - Utilização de estruturas de dados compostas (listas, dicionários, e/ou tuplas) para organização dos dados.
# - Utilização de arquivos para a persistência dos dados cadastrados.
# - Utilização de funções para modularizar as principais funcionalidades da aplicação.
# -o As funções devem ser utilizadas seguindo boas práticas de programação.
# -o Se possível, reaproveitar funções para diferentes módulos do sistema
# (ex.: uma única função para incluir registro de estudantes, professores, disciplinas, turmas e matrículas).
# - Validações de dados e controle de possíveis exceções/erros de execução (try/except).

# IMPORTAÇÕES DE BIBLIOTECAS UTILIZADAS
import json
import os


# FUNÇÕES PARA EXIBIÇÃO DE MENSAGENS PADRONIZADAS
def limpar_tela() -> None:
    """
    Apaga toda a tela para novos desenhos.
    Não recebe parametros
    Sem retorno
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    return None


#  Desenha o menu principal da aplicação. Coloquei em uma função para não poluir o código principal
def desenha_menu_principal() -> None:
    """
    Desenha o menu principal
    não recebe parametros
    sem retorno
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


def desenha_submenu(opcao_principal="OPERAÇÕES") -> None:
    """
    Desenha o menu secundário
    não recebe parametros
    sem retorno
    """
    limpar_tela()
    print("")
    print(f"┌────────────[{opcao_principal:^18}]───────────────┐")
    print("│                                               │")
    print("│ (1) Incluir.                                  │")
    print("│ (2) Listar.                                   │")
    print("│ (3) Editar.                                   │")
    print("│ (4) Excluir.                                  │")
    print("│                                               │")
    print("│ (9) Voltar                                    │")
    print("│                                               │")
    print("└───────────────────────────────────────────────┘")
    return None


def msg_opcao_invalida() -> None:
    """
    Desenha a mensagem de opção inválida
    não recebe parametros
    sem retorno
    """
    print("\t╔════════════════════╗")
    print("\t║   OPÇÃO INVÁLIDA   ║")
    print("\t╚════════════════════╝")
    return None


def msg_saida() -> None:
    """
    Desenha a mensagem de saida do programa
    não recebe parametros
    sem retorno
    """

    limpar_tela()
    print("")
    print(" ╔════════════════════════════════════════════╗")
    print(" ║      Dúvidas e sugestões?                  ║")
    print(" ║      Entre em contato por                  ║")
    print(" ║      handerson.gleber@gmail.com            ║")
    print(" ╚════════════════════════════════════════════╝")
    return None


def msg_abertura() -> None:
    """
    Desenha a mensagem de abertura do programa
    não recebe parametros
    sem retorno
    """

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


def msg_item_nao_encontrado() -> None:
    """
    Desenha a mensagem de item não encontrado
    não recebe parametros
    sem retorno
    """
    print("\t╔══════════════════════════╗")
    print("\t║   Item não encontrado    ║")
    print("\t╚══════════════════════════╝")
    print("")
    msg_enter_continua()

    return None


def msg_em_desenvolvimento() -> None:
    print("")
    print(" ╔════════════════════════════════════════════╗")
    print(" ║            EM DESENVOLVIMENTO              ║")
    print(" ╚════════════════════════════════════════════╝")
    print("")
    msg_enter_continua()


def msg_enter_continua() -> None:
    """
    Padroniza a mensagem "pressione ENTER para continuar".
    Não recebe parametros
    sem retorno
    """
    input("\t Pressione <ENTER> para continuar ...")

    return None


# DEFINIÇÃO DAS FUNÇÕES
def salvar_em_arquivo(dados_param, arquivo_destino_param="itens") -> bool:
    """
    Função para salvar os dados em um arquivo JSON
    Recebe o dicionário com os dados e um nome da base destino.
    Retorna true se tudo certo.
    """
    print(f"\t Salvando dados de: {arquivo_destino_param:.<15}", end=' ')

    try:
        with open("jayzon_" + arquivo_destino_param + ".json", "w", encoding='utf8') as arquivo_escrita:
            json.dump(dados_param, arquivo_escrita, indent=4, ensure_ascii=False)
            print("[Dados salvo com sucesso] ")

    except Exception as erro:
        print(f"*** Erro inesperado  :{erro} ***   ")
        print(f"*** os dados não foram salvos ***  ")
        print("")
        return False

    return True


def abrir_arquivo(arquivo_destino_param="itens", default_keys=("codigo", "nome", "cpf")) -> dict:
    """
    Função para abrir arquivo json
    Recebe o nome do arquivo com os dados
    Retorna dicionario com os dados
    """

    print(f"\t Carregando base de dados: {arquivo_destino_param:.<15}", end=' ')

    # tenta abrir o arquivo de base de dados
    try:
        with open("jayzon_" + arquivo_destino_param + ".json", "r", encoding='utf8') as arquivo_leitura:
            data_return = json.load(arquivo_leitura)
            keys_return = (key for key in data_return[next(iter(data_return))])
            default_keys = keys_return
            print("[Dados carregados com sucesso] ")

    # em caso de erro cria um dicionário com dados de teste
    except Exception as erro:
        print(f"[ {erro} ] Carregando dados de teste ....")
        data_return = popula_dados_teste(arquivo_destino_param, default_keys)
        keys_return = default_keys

    tbl_return = {
        "name": arquivo_destino_param,
        "keys": keys_return,
        "data": data_return
    }

    return tbl_return


def popula_dados_teste(nome_base="item", default_keys=("codigo", "nome", "cpf")) -> dict:
    """
    Função para debug do sistema. Cria um dicionário com dados de teste
    Não recebe parametros
    Retorna dicionario com dados de teste
    """

    dados_teste = dict()

    for i in ('0', '1', '2'):
        for key in default_keys:
            if key == "codigo":
                dados_teste[i]["codigo"] = i
            elif key == "nome":
                dados_teste[i][key] = nome_base + "_" + str(i)
            else:
                dados_teste[i][key] = i

    return dados_teste


def inserir_novo_item(tbl_param) -> bool:
    """
    Insere um item em uma base de dados
    recebe o item que será inserido e o dicionário de destino com os dados
    sem retorno
    """

    novo_item = dict()

    if len(tbl_param["data"]) > 0:
        # pega o id do último item e soma +1
        ultimo_id = next(reversed(tbl_param["data"].keys()))

        chaves = tbl_param["data"][ultimo_id].keys()

        novo_id = str(int(ultimo_id) + 1)

    else:
        novo_id = '0'
        chaves = tbl_param["keys"]

    for chave in chaves:
        if chave == "codigo":
            novo_item[chave] = novo_id
        else:
            novo_item[chave] = input(f"\t Informe o {chave} a ser inserido ")

    # cria um novo item no banco de dados com o código novo
    tbl_param["data"][novo_id] = novo_item

    # lista_param.append(novo_item)
    print(f"\t Item inserido com sucesso: {novo_item} ",)

    return True


def listar_itens(dados_param, nome="itens") -> None:
    """
    Desenha a lista de itens de uma base de dados
    recebe dicionario com os dados e o nome da base
    sem retorno
    """
    limpar_tela()
    print("")

    if len(dados_param) > 0:
        # k = list(dados_param[min(dados_param)].keys())
        titulo = "LISTAR " + nome.upper()
        chaves = [key for key in dados_param[next(iter(dados_param))].keys()]

        if len(chaves) == 3:
            print("┌─────────────────────────────────────────────────────┐")
            print(f"│{titulo:^53}│")
            print("│                                                     │")
            print("├──────────┬─────────────────────────┬────────────────┤")
            print(f"│ {chaves[0].upper():^8} │ {chaves[1].upper():^23} │ {chaves[2].upper():^15}│")  # desenha o cabeçalho (keys) da tabela

            for item in dados_param.values():  # desenha cada linha da tabela
                print("├──────────┼─────────────────────────┼────────────────┤")
                print(f"│ {item[chaves[0]]:^8} │ {item[chaves[1]]:<23} │ {item[chaves[2]]:<15}│")
            print("└──────────┴─────────────────────────┴────────────────┘")
            print("")

        else:
            print("┌────────────────────────────────────┐")
            print(f"│{titulo:^36}│")
            print("│                                    │")
            print("├──────────┬─────────────────────────┤")
            print(
                f"│ {chaves[0].upper():^8} │ {chaves[1].upper():^23} │")  # desenha o cabeçalho (keys) da tabela

            for item in dados_param.values():  # desenha cada linha da tabela
                print("├──────────┼─────────────────────────┤")
                print(f"│ {item[chaves[0]]:^8} │ {item[chaves[1]]:<23} │")
            print("└──────────┴─────────────────────────┘")
            print("")
    else:
        print("┌───────────────────────────────────────────────┐")
        print("│                                               │")
        print("│        *** Não há item cadastrado ***         │")
        print("│                                               │")
        print("└───────────────────────────────────────────────┘")
    return None


def input_codigo() -> str:
    """
    Tratamento da entrada de codigo para consulta alguma base de dados
    Não recebe parametros
    retorna o codigo lido
    """

    # filtro de entrada - laço obriga usuário digitar um número
    while True:
        codigo_busca = input("\n Digite o Codigo do item buscado: ")

        if codigo_busca.isdigit():
            break
        else:
            print("*** Código inválido. **** ")
            print("*** Digite um código númérico. **** ")

    return codigo_busca


def editar_item(dados_param) -> bool:
    """
    Editar o item de uma base dados
    recebe a base de dados
    retorna os dados alterados
    """

    # ler código de destino da alteração
    codigo_item = input_codigo()

    # verifica se existe o item com código informado
    if codigo_item in dados_param:

        # recebe os dados do novo item
        for chave in dados_param[codigo_item].keys():
            if chave == "codigo":
                pass
            else:
                dados_param[codigo_item][chave] = input(f"\t Informe o novo {chave} : ")

        print("\t╔═══════════════════════════════════════════╗")
        print(f"\t║     ITEM  {codigo_item:<4} ATUALIZADO COM SUCESSO     ║")
        print("\t╚═══════════════════════════════════════════╝")

    else:
        msg_item_nao_encontrado()

    return True


def excluir_item(dados_param) -> bool:
    """
    Remover um item de uma base dados
    recebe a base de dados
    retorna a base de dados sem o dado removido
    """

    codigo_item = input_codigo()

    # verifica se existe item com o código informado
    if codigo_item in dados_param:
        # pede confirmação da exclusão

        print("\t╔════════════════════════════════════════════════════════════╗")
        print(f"\t║    tem certeza que deseja excluir {dados_param[codigo_item]['codigo']:^20} ?   ║")
        print("\t╚════════════════════════════════════════════════════════════╝")

        # loop para confirmar exclusão
        while True:

            confirmacao = input("\t Digite [S] para SIM  ou [N] para NÃO ").upper()

            # Resposta SIM - deletar o aluno
            if confirmacao == "S":
                try:
                    del dados_param[codigo_item]

                # se falhar mostra o erro
                except Exception as erro:
                    print("*** Falha inesperada na exclusao do item: ", erro)

                # se funciona exibe mensagem de sucesso
                else:
                    print("\t╔═══════════════════════════════════════════╗")
                    print("\t║         ITEM EXCLUIDO COM SUCESSO         ║")
                    print("\t╚═══════════════════════════════════════════╝")

                # em qualquer caso quebra o loop while de confirmação da exclusão
                finally:
                    break

            # resposta NÃO - cancelar exclusão
            elif confirmacao == "N":
                print("\t╔════════════════════════╗")
                print("\t║   EXCLUSÃO CANCELADA   ║")
                print("\t╚════════════════════════╝")
                break  # quebra o laço while de confirmação da exclusão

            # resposta inválida - nao quebra o loop de confirmação
            else:
                msg_opcao_invalida()

    return True


# FUNÇÃO PRINCIPAL
def main() -> int:
    """
    Função principal do programa
    sem parametros
    retorno o estado final
    """

    # chama mensagem de abertura da aplicação
    msg_abertura()

    print("Carregando arquivos")
    # carrega base de dados da aplicação
    keyset = {
        "alunos":       ("codigo", "nome", "cpf"),
        "professores":  ("codigo", "nome", "cpf"),
        "disciplinas":  ("codigo", "nome"),
        "turmas":       ("codigo", "professor_id", "disciplina_id"),
        "matriculas":   ("codigo", "turma_id", "aluno_id")
    }

    database = {
        "tbl_alunos": abrir_arquivo("alunos", keyset["alunos"]),
        "tbl_professores": abrir_arquivo("professores", keyset["professores"]),
        "tbl_disciplinas": abrir_arquivo("disciplinas", keyset["disciplinas"]),
        "tbl_turmas": abrir_arquivo("turmas", keyset["turmas"]),
        "tbl_matriculas": abrir_arquivo("matrículas", keyset["matriculas"])
    }

    print("Setando configurações")
    running = True

    tbl_destino = dict()
    data_destino = dict()
    chaves_destino = tuple()
    nome_destino = str()

    print("Iniciando menu principal")
    # Loop principal da aplicação. Roda enquanto não receber um BREAK

    while running:  # main app loop

        # loop do menu primário
        while running:

            #  desenha o menu principal
            desenha_menu_principal()

            #  aguarda seleção da opção
            opcao_menu_principal = input("\t Informe o numero da opção desejada:  ")

            # OPÇÃO alunos
            if opcao_menu_principal == '1':

                tbl_destino = database["tbl_alunos"]

                break

            # OPÇÃO professores
            elif opcao_menu_principal == '2':

                tbl_destino = database["tbl_professores"]

                break

            # OPÇÃO disciplinas
            elif opcao_menu_principal == "3":

                tbl_destino = database["tbl_disciplinas"]

                break

            # OPÇÃO turmas
            elif opcao_menu_principal == "4":

                tbl_destino = database["tbl_turmas"]

                break

            # OPÇÃO matriculas
            elif opcao_menu_principal == "5":

                tbl_destino = database["tbl_matriculas"]

                break

            # CASO O USUÁRIO DIGITE OPÇÃO SAIR
            elif opcao_menu_principal == '9' or opcao_menu_principal == 'q':
                msg_saida()

                for tbl in database.values():

                    salvar_em_arquivo(tbl["data"], tbl["name"])

                # salvar_em_arquivo(database["tbl_alunos"]["data"], "alunos")
                # salvar_em_arquivo(database["tbl_professores"]["data"], "professores")
                running = False

            # CASO O USUÁRIO DIGITE OPÇÃO INVALIDA
            else:
                msg_opcao_invalida()

        #  Loop no menu secundário. Roda enquanto não receber um BREAK
        while running:

            nome_destino = tbl_destino["name"]
            chaves_destino = tbl_destino["keys"]
            data_destino = tbl_destino["data"]

            desenha_submenu(nome_destino.upper())

            opcao_submenu1 = input("\t Informe o número da opção desejada: ")

            match opcao_submenu1:
                case "1":  # Opção de INCLUIR

                    inserir_novo_item(tbl_destino)

                    salvar_em_arquivo(data_destino, nome_destino)

                    msg_enter_continua()

                case "2":  # Opção de LISTAR
                    print("\t RELAÇÃO DOS %s CADASTRADOS" % nome_destino)

                    listar_itens(data_destino)

                    msg_enter_continua()

                case "3":  # Opção de EDITAR

                    editar_item(data_destino)

                    salvar_em_arquivo(data_destino, nome_destino)

                    msg_enter_continua()

                case "4":  # Opção de EXCLUIR

                    excluir_item(data_destino)

                    salvar_em_arquivo(data_destino, nome_destino)

                    msg_enter_continua()

                case "9" | "q":  # Opção de SAIR
                    print("Voltando ao menu principal")
                    break

                case _:  # CASO O USUÁRIO DIGITE OPÇÃO INVALIDA
                    msg_opcao_invalida()

    return 0


# INICIO DO PROGRAMA
if __name__ == "__main__":

    print("Iniciando o programa... ")

    main()

    print("Programa finalizado... ")

    exit(0)
