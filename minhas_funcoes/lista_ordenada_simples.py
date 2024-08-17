
# Escrito por  Gr4v4t1nh4
#
# gera uma lista de tamanho aleatório com números inteiros aleatórios
# ordena os valores do menor para o maior
#


import random


## loop principal
while True:

    ## inicia a lista
    lista = []

    ## adiciona um numero aleatório de itens de valor aleatorio
    for i in range(random.randrange(1, 20, 11)):
        lista.append(random.randint(0, 100))

    ## imprime os dados da lista
    print("Lista : ", lista)
    print("\n \t Tamanho da Lista : ", len(lista) )

    ## verificar o maior e o menor numero
    maior_numero = lista[0]
    menor_numero = lista[0]

    for item in lista:
        if item > maior_numero:
            maior_numero = item
        if item < menor_numero:
            menor_numero = item

    print("\t maior número é", maior_numero)
    print("\t menor  número é", menor_numero)

    ## ALGORITMO PARA ORDENAR A LISTA
    trocas = 0

    while True:
        for i in range(int(len(lista)-1)):

            if lista[i] > lista[i+1]:
                #print("index: ", i, "Swap", lista[i], " <>", lista[i]+1)
                lista[i], lista[i+1] = lista[i+1], lista[i]
                trocas += 1
            #else:
                #print("index: ", i)
        if trocas > 0:
            #print("\t Numero de Trocas : ", trocas)
            trocas = 0
            continue
        else:
            #print("\t Trocas : ", trocas, "Lista ordenada")
            break

    print("\n Lista ordenada: ", lista)

    if input("\n Digite 'q' para sair :  ") == "q":
        exit(0)