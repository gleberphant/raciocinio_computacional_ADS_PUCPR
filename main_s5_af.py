## ██████  ██    ██  ██████     ██████  ██████  
# ██   ██ ██    ██ ██          ██   ██ ██   ██ 
# ██████  ██    ██ ██          ██████  ██████  
# ██       ██████   ██████     ██      ██   ██ 

# Curso: Análise e Desenvolvimento de Sistemas
# Disciplina: Raciocínio Computacional (11100010563_20242_02)
# Aluno: HANDERSON GLEBER DE LIMA CAVALCANTI (Gr4v4t1nh4)
# MATRÍCULA 1112024201103

# Atividade Formativa nº 5
#

#


# Esta funcao desenha a mensagem de abertura da aplicação. Coloquei em uma função para não poluir o código principal

if __name__ == "__main__":
    # modelo de dicionario de aluno = {'código':'','nome':'','cpf':''}
    lista_alunos = []  # popula o banco com dados de teste

    for i in range(5):
        lista_alunos.append({"codigo": 11 * i, "nome": "teste_" + str(i), "cpf": str(i) * 6})

    print("\t ..............................................")
    print("\t :..BEM VINDO AO SISTEMA DE GESTÃO ACADÊMICA..:")
    print("\t :.......Desenvolvido por : Gravatinha........:")
    print("\t ..............................................")

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

        opcao_menu_principal = input("\t Informe o numero da opção desejada:  ")[0]

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
                        novo_aluno = {"codigo": len(lista_alunos), "nome": input("\t Informe o NOME a ser inserido:  "),
                                      "cpf": input("\t Informe o CPF a ser inserido:  ")}

                        lista_alunos.append(novo_aluno)

                    case '2':  # Opção de listar
                        print("\t \t RELAÇÃO DOS ALUNOS CADASTRADOS")
                        print("\t ___________________________________________")
                        for item in lista_alunos:
                            for k, v in item.items():
                                print("\t |{}\t: {}  ".format(k, v))
                            print("\t -------------------")
                        print("\t ____________________________________________")

                        input("\t pressione <ENTER> para continuar")

                    case '3':  # Opção de ATUALIZAR
                        codigo_atualizar = input("\n \t Digite o Codigo do aluno que deseja atualizar: ")

                        item_encontrado = False

                        if codigo_atualizar.isnumeric() is True:
                            for item in lista_alunos:
                                if int(codigo_atualizar) == item["codigo"]:
                                    item_encontrado = True
                                    item["nome"] = input("\n Digite o novo nome: ").upper()
                                    item["cpf"] = input("\n Digite o novo CPF: ").upper()
                                    print("\t item atualizado com sucesso")

                            if not item_encontrado:
                                print("\t aluno nao foi encontrado")
                        else:
                            print("\n \t Valor inválido \n ")

                        input("\t pressione <ENTER> para continuar")

                    case '4':  # Opção de EXCLUIR

                        codigo_remover = input("\n \t Digite o Codigo do aluno para remover: ")
                        item_encontrado = False

                        if codigo_remover.isnumeric() is True:
                            for item in lista_alunos:
                                if codigo_remover == str(item["codigo"]):
                                    item_encontrado = True
                                    print(f"\t Voce tem certeza que deseja excluir ? Codigo {1} - Nome {2}: ",
                                          item["codigo"], item["nome"])

                                    if input("S ou N").upper() == "S":
                                        lista_alunos.remove(item)
                                        print(f"\t Código {1} excluido com sucesso ", codigo_remover)

                            if not item_encontrado:
                                print("Nenhum item foi encontrado com esse codigo")
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

            print("\t *** EM DESENVOLVIMENTO **** ")
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
