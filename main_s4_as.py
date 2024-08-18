""" sitema de gestão academica - pucpr VS4"""
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
# │   Atividade Somativa 1 - semana 4                           │
# └─────────────────────────────────────────────────────────────┘

# CRITÉRIOS
# - Desenvolva as funcionalidades de incluir e listar estudantes
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

    lista_alunos = []

    for i in range(5):  # popula o banco com dados de teste
        lista_alunos.append("Aluno_" + str(i))

    print("")
    print(" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print(" ░░░░░░░░░░SISTEMA DE GESTÃO ACADÊMICA░░░░░░░░")
    print(" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print(" ░░░░ por: HANDERSON GLEBER (gravatinha) ░░░░░")
    print(" ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("")

    while True:  # Loop principal da aplicação. Roda enquanto não receber um BREAK

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

        opcao_menu_principal = input(" Informe o numero da opção desejada: ")

        if opcao_menu_principal == '1':  # ENTRA NO MENU DE ESTUDANTE

            while True:  # Loop no menu secundário. Roda enquanto não receber um BREAK

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

                opcao_submenu1 = input(" Informe o número da opção desejada: ")

                match opcao_submenu1:
                    case '1':  # Opção de incluir
                        novo_aluno = input("\t Informe o NOME a ser inserido:  ")
                        lista_alunos.append(novo_aluno)

                    case '2':  # Opção de listar
                        print("")
                        print("┌───────────────────────────────────────────────┐")
                        print("│        RELAÇÃO DOS ALUNOS CADASTRADOS         │")
                        if len(lista_alunos) > 0:
                            for i, aluno in enumerate(lista_alunos):
                                print("│                                               │")
                                print(f"│ Cod. [{i:^5}]  -  Nome [ {aluno:<18} ]  │")
                            print("│                                               │")
                            print("└───────────────────────────────────────────────┘")
                        else:
                            print("\t Não há estudantes cadastrados ")

                        input("\t pressione <ENTER> para continuar")

                    case '3':  # Opção de ATUALIZAR
                        try:
                            codigo_atualizar = int(input("\n Digite o Codigo do aluno que deseja atualizar : "))
                        except ValueError:
                            print("\t╔════════════════════╗")
                            print("\t║   OPÇÃO INVÁLIDA   ║")
                            print("\t╚════════════════════╝")
                        else:
                            if codigo_atualizar < len(lista_alunos):
                                lista_alunos[codigo_atualizar] = input("\n\t Digite o novo nome : ").upper()
                                print("\n\t *****  ITEM ATUALIZADO COM SUCESSO  ***** \n")
                            else:
                                print("\t╔════════════════════╗")
                                print("\t║   OPÇÃO INVÁLIDA   ║")
                                print("\t╚════════════════════╝")

                        input("\t pressione <ENTER> para continuar")
                    case '4':  # Opção de EXCLUIR
                        try:
                            codigo_remover = int(input("\n Digite o Codigo do aluno para remover: "))
                        except ValueError:
                            print("\t╔════════════════════╗")
                            print("\t║   OPÇÃO INVÁLIDA   ║")
                            print("\t╚════════════════════╝")
                        else:
                            if codigo_remover < len(lista_alunos):
                                print("\t")
                                print("\t╔══════════════════════════════════════════════════╗")
                                print("\t║   Voce tem certeza que deseja excluir o item ?   ║")
                                print("\t╚══════════════════════════════════════════════════╝")
                                print("\t")
                                if input("\t \t Digite [S] para SIM  ou [N] para NÃO ").upper() == "S":
                                    del lista_alunos[codigo_remover]
                                    print("\n *****  Exclusão realizada com sucesso ***** \n")
                                else:
                                    print("\n *****  Exclusão cancelada  ***** \n")
                            else:
                                print("\t╔════════════════════╗")
                                print("\t║   OPÇÃO INVÁLIDA   ║")
                                print("\t╚════════════════════╝")
                        input(" pressione <ENTER> para continuar")
                    case '9':  # Opção de SAIR
                        break
                    case _:  # CASO O USUÁRIO DIGITE OPÇÃO INVALIDA
                        print("\t╔════════════════════╗")
                        print("\t║   OPÇÃO INVÁLIDA   ║")
                        print("\t╚════════════════════╝")

        elif (opcao_menu_principal == '2'
              or opcao_menu_principal == '3'
              or opcao_menu_principal == '4'
              or opcao_menu_principal == '5'):  # OUTROS MODULOS DO MENU PRINCIPAL

            print("")
            print(" ╔════════════════════════════════════════════╗")
            print(" ║            EM DESENVOLVIMENTO              ║")
            print(" ╚════════════════════════════════════════════╝")
            print("")
            input(" pressione ENTER para continuar")

        elif opcao_menu_principal == '9' or opcao_menu_principal == 'q':  # OPÇÃO SAIR DO MENU PRINCIPAL
            print(" ╔════════════════════════════════════════════╗")
            print(" ║      Dúvidas e sugestões?                  ║")
            print(" ║      Entre em contato por                  ║")
            print(" ║      handerson.gleber@gmail.com            ║")
            print(" ╚════════════════════════════════════════════╝")
            break

        else:  # CASO O USUÁRIO DIGITE OPÇÃO INVALIDA
            print("\n \t Opção inválida \n ")

    exit(0)
