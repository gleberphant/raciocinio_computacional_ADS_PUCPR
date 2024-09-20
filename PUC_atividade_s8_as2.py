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
# - Professores
# - Código do professor (Número inteiro)
# - Nome do professor (String)
# - CPF do professor (String)
# - Disciplinas
# - Código da disciplina (Número inteiro)
# - Nome da disciplina (String)
# - Turmas
# - Código da turma (Número inteiro)
# - Código do professor (Número inteiro)
# - Código da disciplina (Número inteiro)
# - Matrículas
# - Código da turma (Número inteiro)
# - Código do estudante (Número inteiro)
# - Validação de dados na manipulação de turmas e matrículas (verificar se um código já existe antes de incluir uma
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

# importações de bibliotecas utilizadas
import json
import os

# base de dados
# db_alunos = {}


# funções
def salvar_em_arquivo(dados_param, nome_arquivo_destino_param="itens") -> bool:
    """
    Função para salvar os dados em um arquivo JSON
    Recebe o dicionário com os dados e um nome da base destino.
    Retorna true se tudo certo.
    """
    print("salvando dados de ", nome_arquivo_destino_param, " ... ", end=' ')

    try:
        with open("jayzon_" + nome_arquivo_destino_param + ".json", "w", encoding='utf8') as arquivo_escrita:
            json.dump(dados_param, arquivo_escrita, ensure_ascii=False)
            print("Dados salvo com sucesso ")

    except Exception as erro:
        print(f"***** Erro inesperado  :{erro} **** \n  ")
        print(f"***** os dados não foram salvos **** \n  ")
        return False

    return True


def abrir_arquivo(nome_base_destino_param="itens") -> dict:
    """
    Função para abrir arquivo json
    Recebe o nome do arquivo com os dados
    Retorna dicionario com os dados
    """

    print(" [ Abrindo arquivo : ", nome_base_destino_param, " ... ] ", end='\n')

    # tenta abrir o arquivo de base de dados
    try:
        with open("jayzon_" + nome_base_destino_param + ".json", "r", encoding='utf8') as arquivo_leitura:
            data_return = json.load(arquivo_leitura)

    # em caso de erro cria um dicionário com dados de teste
    except Exception as erro:
        print(f"***** Erro inesperado  :{erro} **** \n  ")
        print("[ Carregando dados de teste .... ]")

        data_return = popula_dados_teste()
        salvar_em_arquivo(data_return)

    return data_return


def popula_dados_teste() -> dict:
    """
    Função para debug do sistema. Cria um dicionário com dados de teste
    Não recebe parametros
    Retorna dicionario com dados de teste
    """
    dados_teste = {}

    for i in range(8):
        dados_teste[str(i)] = {"codigo": str(i), "nome": "aluno_" + str(i), "cpf": str(i) * 6}

    return dados_teste


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


def mostra_submenu() -> None:
    """
    Desenha o menu secundário
    não recebe parametros
    sem retorno
    """
    limpar_tela()
    print("")
    print("┌──────────────[ MENU OPERAÇÕES ]───────────────┐")
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
    input(" pressione <ENTER> para continuar")

    return None


def msg_enter_continua() -> None:
    """
    Desenha de modo padrão a mensagem "pressione ENTER para continuar".
    Não recebe parametros
    sem retorno
    """
    input("\t Pressione <ENTER> para continuar ...")
    return None


def inserir_novo_item(novo_item, dados_param) -> bool:
    """
    Insere um item em uma base de dados
    recebe o item que será inserido e o dicionário de destino com os dados
    sem retorno
    """
    if len(dados_param) > 0:
        # pega o id do último item e soma +1
        novo_id = int(next(reversed(dados_param.keys()))) + 1
    else:
        novo_id = 0

    # define o código do item como sendo o novo id
    novo_item['codigo'] = novo_id

    # cria um novo item no banco de dados com o código novo
    dados_param[str(novo_id)] = novo_item

    # lista_param.append(novo_item)
    print(f"\t Item inserido com sucesso: \n \t {1} ", novo_item['nome'])

    salvar_em_arquivo(dados_param)

    return True


def listar_itens(dados_param, nome="itens") -> None:
    """
    Desenha a lista de itens de uma base de dados
    recebe dicionario com os dados e o nome da base
    sem retorno
    """
    limpar_tela()
    print("")
    print("┌───────────────────────────────────────────────┐")
    print("│            LISTAR {0:<11}                 │".format(nome.upper()))
    print("│                                               │")
    if len(dados_param) > 0:
        k = list(dados_param[min(dados_param)].keys())

        print("├────────┬─────────────────────────┬────────────┤")
        print(f"│ {k[0]:<6} │ {k[1]:<23} │ {k[2]:<11}│")  # desenha o cabeçalho (keys) da tabela

        for item in dados_param.values():  # desenha cada linha da tabela
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


def editar_item(dados_param) -> dict:
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
        novo_item = {'codigo': codigo_item,
                     'nome': input("\n Digite o novo nome: "),
                     'cpf': input("\n Digite o novo CPF: ")}

        # tenta atualizar o aluno
        try:
            dados_param[codigo_item] = novo_item
            salvar_em_arquivo(dados_param)

        # se falhar mostra o erro
        except Exception as erro:
            print(" *** ocorreu um erro quando estava atualizando o aluno **** \n Erro = ", erro)

        # se funcionar exibe mensagem de sucesso
        else:
            print("\t╔═══════════════════════════════════════════╗")
            print(f"\t║ *** ITEM  {novo_item['codigo']:<4} ATUALIZADO COM SUCESSO *** ║")
            print("\t╚═══════════════════════════════════════════╝")
    else:
        msg_item_nao_encontrado()

    return dados_param


def remover_item(dados_param) -> dict:
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
        print(f"\t║    tem certeza que deseja excluir {dados_param[codigo_item]['nome']:^20} ?   ║")
        print("\t╚════════════════════════════════════════════════════════════╝")

        # loop para confirmar exclusão
        while True:

            confirmacao = input("\t Digite [S] para SIM  ou [N] para NÃO ").upper()

            # Resposta SIM - deletar o aluno
            if confirmacao == "S":
                try:
                    del dados_param[codigo_item]
                    salvar_em_arquivo(dados_param)

                # se falhar mostra o erro
                except Exception as erro:
                    print("*** falha na exclusao *** \n Erro :", erro)

                # se funciona exibe mensagem de sucesso
                else:
                    print("\t╔═══════════════════════════════════════════╗")
                    print("\t║   ****  ITEM EXCLUIDO COM SUCESSO  ****   ║")
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

    return dados_param


# Função principal
def main() -> int:
    """
    Função principal do programa
    sem parametros
    retorno o estado final
    """

    # chama mensagem de abertura da aplicação
    msg_abertura()

    # carrega base de dados da aplicação
    db_alunos = abrir_arquivo()
    db_professores = {}

    # Loop principal da aplicação. Roda enquanto não receber um BREAK
    while True:

        #  desenha o menu principal
        desenha_menu_principal()

        #  aguarda seleção da opção
        opcao_menu_principal = input("\t Informe o numero da opção desejada:  ")[0]

        # ENTRA NO MENU DE ESTUDANTE
        if (opcao_menu_principal == '1'
                or opcao_menu_principal == '2'):

            # inicia variáveis
            destino = ""
            db_destino = {}
            novo_item = {'codigo': ''}
            campos = []

            if opcao_menu_principal == "1":
                destino = "alunos"
                campos = ["nome", "cpf"]
                db_destino = db_alunos

            elif opcao_menu_principal == "2":
                destino = "professores"
                campos = ["nome", "cpf"]
                db_destino = db_professores

            #  Loop no menu secundário. Roda enquanto não receber um BREAK
            while True:

                mostra_submenu()

                opcao_submenu1 = input("\t Informe o número da opção desejada: ")

                match opcao_submenu1:
                    case "1":  # Opção de INCLUIR

                        for campo in campos:
                            novo_item[campo] = input("\t Informe o %s a ser inserido" % campo)

                        inserir_novo_item(novo_item, db_destino)

                        msg_enter_continua()

                    case "2":  # Opção de LISTAR
                        print("\t RELAÇÃO DOS %s CADASTRADOS" % destino)

                        listar_itens(db_destino)

                        msg_enter_continua()

                    case "3":  # Opção de EDITAR

                        db_alunos = editar_item(db_alunos)

                        msg_enter_continua()

                    case "4":  # Opção de EXCLUIR

                        db_alunos = remover_item(db_alunos)

                        msg_enter_continua()

                    case "9" | "q":  # Opção de SAIR
                        print("Voltando ao menu principal")
                        break

                    case _:  # CASO O USUÁRIO DIGITE OPÇÃO INVALIDA
                        msg_opcao_invalida()

        elif (opcao_menu_principal == "5"
              or opcao_menu_principal == "3"
              or opcao_menu_principal == "4"):  # OUTROS MODULOS DO MENU PRINCIPAL

            print("")
            print(" ╔════════════════════════════════════════════╗")
            print(" ║            EM DESENVOLVIMENTO              ║")
            print(" ╚════════════════════════════════════════════╝")
            print("")
            msg_enter_continua()

        # OPÇÃO SAIR DO MENU PRINCIPAL
        elif opcao_menu_principal == "9" or opcao_menu_principal == "q":
            msg_saida()
            salvar_em_arquivo(db_alunos)
            break

        # CASO O USUÁRIO DIGITE OPÇÃO INVALIDA
        else:
            msg_opcao_invalida()

    return 0


# Inicia o programa
if __name__ == "__main__":
    print("Iniciando o programa... ")
    main()
    print("Programa finalizado... ")
    exit(0)
