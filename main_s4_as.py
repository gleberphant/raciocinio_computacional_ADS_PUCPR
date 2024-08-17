""" sitema de gestão academica - pucpr"""

# ██████  ██    ██  ██████     ██████  ██████
# ██   ██ ██    ██ ██          ██   ██ ██   ██
# ██████  ██    ██ ██          ██████  ██████
# ██       ██████   ██████     ██      ██   ██

# Curso: Análise e Desenvolvimento de Sistemas
# Disciplina: Raciocínio Computacional (11100010563_20242_02)
# Aluno: HANDERSON GLEBER DE LIMA CAVALCANTI (Gr4v4t1nh4)
# MATRÍCULA 1112024201103
#
#
# Atividade Somativa 1 - semana 4
#

# Desenvolva as funcionalidades de incluir e listar estudantes
# - Apenas o nome do estudante deve ser perguntado ao usuário
# - Os nomes dos estudantes devem ser armazenados em uma lista.
# - Para a funcionalidade de listar, deve ser utilizada uma estrutura de repetição para percorrer a lista
# - e mostrar os nomes cadastrados – ver Figura 1.
# - Caso a lista de estudantes esteja vazia quando a opção de listar for acionada, deve-se mostrar uma mensagem
# - “Não há estudantes cadastrados”.
# - Caso o usuário selecione as opções professores, disciplinas, turmas ou matrículas no menu principal,
# - o sistema deve mostrar a mensagem “EM DESENVOLVIMENTO”, e mostrar novamente o menu principal.
# - Caso o usuário selecione as opções atualizar ou excluir no menu de operações do estudante,
# - o sistema deve mostrar a mensagem “EM DESENVOLVIMENTO”, e mostrar novamente o menu de operações.


if __name__ == "__main__":

    lista_alunos = [ ]

    for i in range(5):  # popula o banco com dados de teste
        lista_alunos.append("Aluno_" + str(i))

    print("\n \n")
    print("\t --------------------------------------------")
    print("\t ............................................")
    print("\t ....... SISTEMA DE GESTÃO ACADÊMICA.........")
    print("\t ............................................")
    print("\t .............por: Gravatinha................")
    print("\t ............................................")
    print("\t --------------------------------------------")
    print("\n \n")

    while True:  # Loop principal da aplicação. Roda enquanto não receber um BREAK

        print("\t -------------- MENU PRINCIPAL --------------- ")
        print("\t|                                             |")
        print("\t| (1) Gerenciar Estudantes.                   |")
        print("\t| (2) Gerenciar Professores.                  |")
        print("\t| (3) Gerenciar Disciplinas.                  |")
        print("\t| (4) Gerenciar Turmas.                       |")
        print("\t| (5) Gerenciar Matrícula.                    |")
        print("\t|                                             |")
        print("\t| (9) Sair.                                   |")
        print("\t|                                             |")
        print("\t --------------------------------------------- ")

        opcao_menu_principal = input("\t Informe o numero da opção desejada:  ")

        if opcao_menu_principal == '1':  # ENTRA NO MENU DE ESTUDANTE

            while True:  # Loop no menu secundário. Roda enquanto não receber um BREAK

                print("\t*************** MENU OPERAÇÕES ******************")
                print("\t*                                               *")
                print("\t* (1) Incluir.                                  *")
                print("\t* (2) Listar.                                   *")
                print("\t* (3) Atualizar.                                *")
                print("\t* (4) Excluir.                                  *")
                print("\t*                                               *")
                print("\t* (9) Voltar                                    *")
                print("\t*                                               *")
                print("\t*************************************************")

                opcao_submenu1 = input("\t Informe o número da opção desejada: ")

                match opcao_submenu1:
                    case '1':  # Opção de incluir
                        novo_aluno = input("\t Informe o NOME a ser inserido:  ")
                        lista_alunos.append(novo_aluno)

                    case '2':  # Opção de listar
                        print("\t \t RELAÇÃO DOS ALUNOS CADASTRADOS")
                        print("\t ___________________________________________")
                        if len(lista_alunos) > 0:
                            for i, aluno in enumerate(lista_alunos):
                                print(f"\t |Num.: {0} - Nome:{1} ", i, aluno)
                                print("\t -------------------")
                            print("\t ____________________________________________")
                        else:
                            print("Não há estudantes cadastrados ")

                        input("\t pressione <ENTER> para continuar")

                    case '3':  # Opção de ATUALIZAR
                        try:
                            codigo_atualizar = int(input("\n \t Digite o Codigo do aluno que deseja atualizar: "))
                        except ValueError:
                            print("\n \t Valor inválido \n ")
                        else:
                            if codigo_atualizar < len(lista_alunos):
                                lista_alunos[codigo_atualizar] = input("\n Digite o novo nome: ").upper()
                                print("\t item atualizado com sucesso")
                            else:
                                print("\n \t Valor inválido \n ")

                        input("\t pressione <ENTER> para continuar")
                    case '4':  # Opção de EXCLUIR
                        try:
                            codigo_remover = int(input("\n \t Digite o Codigo do aluno para remover: "))
                        except ValueError:
                            print("\n \t Valor inválido \n ")
                        else:
                            if codigo_remover < len(lista_alunos):
                                print("\t Voce tem certeza que deseja excluir ?")
                                if input("\t Digite [S] para sim  ou [N] para não").upper() == "S":
                                    del lista_alunos[codigo_remover]
                                    print("\t Exclusão com sucesso ")
                                else:
                                    print("\t Exclusão cancelada")
                            else:
                                print("\n \t Valor inválido \n ")
                        input("\t pressione <ENTER> para continuar")
                    case '9':  # Opção de SAIR
                        print("\t Voltando ao menu principal")
                        break
                    case _:  # CASO O USUÁRIO DIGITE OPÇÃO INVALIDA
                        print("\n \t Opção inválida  \n ")

        elif (opcao_menu_principal == '2' or
              opcao_menu_principal == '3' or
              opcao_menu_principal == '4' or
              opcao_menu_principal == '5'):  # OUTROS MODULOS DO MENU PRINCIPAL

            print("\t **********************************************")
            print("\t *** EM DESENVOLVIMENTO **** ")
            print("\t **********************************************")
            print("\t \n")
            input("\t pressione ENTER para continuar")

        elif opcao_menu_principal == '9' or opcao_menu_principal == 'q':  # OPÇÃO SAIR DO MENU PRINCIPAL
            print("\t **********************************************")
            print("\t*      Dúvidas e sugestões?                   *")
            print("\t*      Entre em contato por                   *")
            print("\t*      handerson.gleber@gmail.com             *")
            print("\t***********************************************")
            break

        else:  # CASO O USUÁRIO DIGITE OPÇÃO INVALIDA
            print("\n \t Opção inválida \n ")

    exit(0)
