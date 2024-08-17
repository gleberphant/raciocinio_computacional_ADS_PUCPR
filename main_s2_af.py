if __name__ == "__main__":

	print(
	"""
    .............................................. 
    :..BEM VINDO AO SISTEMA DE GESTÃO ACADÊMICA..:
    :.......Desenvolvido por : Gravatinha........:
    .............................................. 
    
        """)


	print(
	"""
	 --------------- MENU PRINCIPAL -------------- 
	|                                             |
	| (1) Gerenciar Estudantes.                   |
	| (2) Gerenciar Professores.                  |
	| (3) Gerenciar Disciplinas.                  |
	| (4) Gerenciar Turmas.	                      |
	| (5) Gerenciar Matrícula.                    |
	|                                             |
	| (9) Sair.                                   |
	|                                             |
	----------------------------------------------- 
	""")

	opcao_menu_principal = input("\t Informe o numero da opção desejada:  ")

	if opcao_menu_principal == "1" or opcao_menu_principal == "2" or opcao_menu_principal == "3" or opcao_menu_principal == "4"or opcao_menu_principal == "5":
		print(
			"""
            *************************************************
            *            MENU [{}] DE OPERAÇÕES 
            *                                               *
            * (1) Incluir.                                  *
            * (2) Listar.                                   *
            * (3) Atualizar.                                *
            * (4) Excluir.                                  *
            *                                               *
            * (9) Voltar                                    *
            *                                               *
            *************************************************
            """.format(opcao_menu_principal))

		opcao_submenu1 = input("\t Informe o número da opção desejada: ")

		if opcao_submenu1 == "1" or opcao_submenu1 == "2" or opcao_submenu1 == "3" or opcao_submenu1 == "4"or opcao_submenu1 == "9":
			print(
				"""
				.............................................. 
				:.............EM DESENVOLVIMENTO ..............:
				.............................................. 

				""")
		else:
			print(
				"""
                !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                !!  OPÇÃO INVÁLIDA                            !!
                !!  :digite um valor válido                   !!
                !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                """)
			exit(0)
	
	elif opcao_menu_principal == "9":

		print(
			"""
            ***********************************************
            *                                             *
            *      Dúvidas e sugestões?                   *
            *                                             *
            *      Entre em contato por                   *
            *                                             *
            *      handerson.gleber@gmail.com             *
            *                                             *
            ***********************************************
            \n \a """)

		exit(0)
		
	else:
		print(
			"""
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            !!  OPÇÃO INVÁLIDA                            !!
            !!  :digite um valor válido                   !!
            !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            """)
		exit(0)
