
# Escrito por  Gr4v4t1nh4
#
# gera uma lista de tamanho aleatorio com numeros inteiros aleatorios
#


import random

# iniciar lista de numeros random

while True:
    lista = []


    for i in range(random.randint(1, 20)):
        lista.append(random.randint(0, 100))

    print("Lista : ", lista)
    print("\n \t Tamanho da Lista : ", len(lista))

    maior_numero = lista[0]
    menor_numero = lista[0]

    for i in lista:
        if i > maior_numero:
            maior_numero = i
        if i < menor_numero:
            menor_numero = i

    print("\t maior número é", maior_numero)
    print("\t menor  número é", menor_numero)

    if input("\n Digite 'q' para sair :  ") == "q":
        exit(0);