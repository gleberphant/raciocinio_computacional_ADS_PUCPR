
# recebe data nascimento
data_nascimento = input("Digite sua data de nascimento no formato dd/mm/aaaa:")


# recebe data atual
data_atual = input("digite a data atual no formato dd/mm/aaaa: ")

# separa a data de nascimento em  em dia mes ano

dia_nascimento = int(data_nascimento[:2])
mes_nascimento = int(data_nascimento[3:5])
ano_nascimento = int(data_nascimento[6:])


# separa a data atual em dia mes ano
dia_atual = int(data_atual[:2])
mes_atual = int(data_atual[3:5])
ano_atual = int(data_atual[6:])


# calculo da idade
# diferença entre anos
idade = ano_atual - ano_nascimento 

# verifica mes. se ja fez aniversario ou não
if mes_nascimento > mes_atual:
	idade -= 1
elif mes_nascimento==mes_atual and dia_nascimento > dia_atual:
	idade -= 1


# mostra adiferenca

print(f"Sua idade é : {idade} ")

input("\n pressione qualquer tecla para sair ......")
