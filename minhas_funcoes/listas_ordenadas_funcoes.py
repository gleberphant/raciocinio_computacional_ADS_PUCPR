
# Escrito por  Gr4v4t1nh4
#
# diferentes funções para ordenação de listas
# ordena os valores do menor para o maior
#


import random


#funcao ordenar lista simples
def ordena_lista_simples(lista_param):
	big_O = 0 #notacao bigO
	trocas = 0

	while True:
		for i in range(len(lista_param) - 1):
			big_O+=1
			if lista_param[i] > lista_param[i + 1]:
				lista_param[i], lista_param[i + 1] = lista_param[i + 1], lista_param[i]
				trocas += 1

		if trocas > 0:
			trocas = 0
			continue
		else:
			break

	print("TEMPO Big O : {}".format(big_O))
	return lista_param

#função quicksort
def ordena_quicksort(lista_param):
	big_O = 0
	if len(lista_param)  < 2 :
		return lista_param
	else:
		lista_menores = []
		lista_maiores = []
		for item in lista_param[1:]:
			big_O += 1
			if item <= lista_param[0]:
				lista_menores.append(item)
			elif item > lista_param[0]:
				lista_maiores.append(item)

		#print(" lista menor ", lista_menores, " pivo ", lista_param[0], " lista maior ", lista_maiores)
		print("TEMPO Big O : {}".format(big_O))
		return ordena_quicksort(lista_menores) + [lista_param[0]] + ordena_quicksort(lista_maiores)





#funcao descobrir maior ou menor
def encontra_maior_valor(lista_param):
	maior_valor = lista_param[0]

	for item in lista_param:
		if item > maior_valor:
			maior_valor = item

	return maior_valor

def encontra_menor_valor(lista_param):
	menor_valor = lista_param[0]

	for item in lista_param:
		if item < menor_valor:
			menor_valor = item
	return menor_valor

def cria_lista_aleatoria(minimo=4, tamanho=10, passo=1):
	nova_lista = []		#cria lista vazia

	for item in range(random.randrange(minimo, tamanho, passo)): #cria quantidade aleatoria de itens
		nova_lista.append(random.randint(0,100)) #gera um item aleatorio

	return nova_lista #retorna a lista criada

## main
if __name__ == "__main__":
	while True:
		## inicia a lista
		lista = cria_lista_aleatoria()

		lista_ordenada =  ordena_quicksort(lista)
		## imprime os dados da lista

		print("")
		print("Lista Inicial : ", lista)
		print("Lista Ordenada : ", ordena_quicksort(lista))
		print("Lista Ordenada 2 : ", ordena_lista_simples(lista))
		print("")
		print("\t Tamanho da Lista : ", len(lista_ordenada) )
		print("\t Maior valor é: ",encontra_maior_valor(lista))
		print("\t Menor  valor é: ", encontra_menor_valor(lista))


		if input("\n Digite 'q' para sair :  ") == "q":
			exit(0)