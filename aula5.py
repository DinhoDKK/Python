lista = [12,10,5,7]
lista_animal = ['cachorro', 'gato', 'elefante','lobo','arara']

#PARA VALORES IMUTAVEIS
tupla = (1,10,12,14)
print(tupla)

#CONVERTER LISTA EM TUPLA
tupla_animal = tuple(lista_animal)
print(tupla_animal)
#CONVERTER TUPLA EM LISTA
lista_numerica = list(tupla)
print(lista_numerica)


#CONTADOR DE ELEMENTOS
print(len(tupla))
print(len(lista_animal))



# #ORDENANDO A LISTA
# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# #ORDERNAR DE FORMA CONTRARIA
# lista_animal.reverse()
# print(lista_animal)

# print(lista_animal[1])
#
# for x in lista_animal:
#     print(x)
#
# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# #SOMA DE VALORES DA LISTA
# print(soma)
# #METODO PARA SOMAR NUMEROS DA LISTA
# print(sum(lista))
# #MAIOR NUMERO DA LISTA
# print(max(lista))
# #MENOR VALOR
# print(min(lista))
# #MAIOR VALOR STRING CRITERIO É A ORDEM ALFABETICA
# print(max(lista_animal))
# #MENOR VALOR STRING CRITERIO É A ORDEM ALFABETICA
# print(min(lista_animal))

# if 'lobo' in lista_animal:
#     print('Existe um lobo na lista')
# else:
#     print('Nao existe um lobo na lista. Sera incluido')
#     #ADICIONAR UM VALOR NA LISTA
#     lista_animal.append('lobo')
#     print(lista_animal)

# #RETIRAR O ULTIMO VALOR DA LISTA ou coloco a posição .pop(1)
# lista_animal.pop()
# print(lista_animal)

# #REMOVER ATRAVES DO NOME
# lista_animal.remove('elefante')
# print(lista_animal)

#MULTIPLICAR VALORES
# nova_lista = lista_animal * 3
# print(nova_lista)