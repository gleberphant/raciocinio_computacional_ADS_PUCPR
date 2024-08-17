# 
#
# Curso: Análise e Desenvolvimento de Sistemas
# Aluno: Handerson Gleber de Lima Cavalcanti (Gr4v4t1nh4)
#



if __name__ == "__main__":
	#Mensagem de boas vindas
	print(
	"""
    .............................................. 
    :..BEM VINDO AO SISTEMA DE GESTÃO ACADÊMICA..:
    :.......Desenvolvido por : Gravatinha........:
    .............................................. 
    
        """)

	#loop principal
	while True:
		#menu principal	
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
		
		#condicional de menus secundarios|
		if opcao_menu_principal == "1" or opcao_menu_principal == "2" or opcao_menu_principal == "3" or opcao_menu_principal == "4"or opcao_menu_principal == "5":
			
			#loop secundario
			while True:	
		
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

				#opcoes dos menu secundario
				if opcao_submenu1 == "1" or opcao_submenu1 == "2" or opcao_submenu1 == "3" or opcao_submenu1 == "4":
					print(
						"""
						.............................................. 
						:.............EM DESENVOLVIMENTO ..............:
						.............................................. 

						""")
				#opcao sair menu secundário
				elif opcao_submenu1 == "9":
					print("Voltando ao menu principal")
					break
				
				#opcao invalida
				else:
					print ("\t ---  OPÇÃO INVÁLIDA  --- \n" )
					input ("\t\t pressione <ENTER> para continua" )
					break
		
		#opcao sair menu principal
		elif opcao_menu_principal == "9":
			print(
			"""
			***********************************************
			*      Dúvidas e sugestões?                   *
			*      Entre em contato por                   *
			*      handerson.gleber@gmail.com             *
			***********************************************
			\n \a """)
			break
		
		#opcao invalida menu principal	
		else:
			print ("\t ---  OPÇÃO INVÁLIDA  --- \n" )
			input ("\t\t pressione <ENTER> para continua" )
			
	