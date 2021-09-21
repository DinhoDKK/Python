#Conjuntos e Subconjuntos
conjunto = {1,2,3,4,5}
conjunto2 = {6,7,8,5}
#Uniao entre dois conjuntos
conjunto_uniao = conjunto.union(conjunto2)
print('Uniao: {} '.format(conjunto_uniao))
#Inteseção entre dois conjuntos
conjunto_intersecao = conjunto.intersection(conjunto2)
print('Interseção: {}' .format(conjunto_intersecao))
#Diferença entre dois conjuntos
conjunto_diferenca = conjunto.difference(conjunto2)
print('Diferenca entre 1 e 2: {} ' .format(conjunto_diferenca))
#######
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 2 e 1: {}' .format(conjunto_diferenca2))

#Diferença simétrica
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença Simetrica: {}' .format(conjunto_diff_simetrica))

#SUBSET: se o conjunto a esta dentro do conjunto b
conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é um subconjunto de B : {} ' .format(conjunto_subset))
#SUPERSET: se o conjunto b esta contendo o conjunto a
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A: {}' .format(conjunto_superset))

#TIRANDO A DUPLICIDADE E CONVERTENDO LISTA EM CONJUNTO E VICE E VERSA
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)


# conjunto = {1,2,3,4}
# conjunto.add(5)     #adicionar
# conjunto.discard(2) #remover
# print(conjunto)