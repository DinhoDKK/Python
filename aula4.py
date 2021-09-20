#Laços de repetição

#WHILE PARA A RESOLUÇÃO DA AULA 3
a = int(input('Primeiro Bimestre: '))
while a > 10:
    a = int(input('Voce digitou uma nota maior que 10! Primeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
while b > 10:
    b = int(input('Voce digitou uma nota maior que 10! Segundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
while c > 10:
    c = int(input('Voce digitou uma nota maior que 10! Terceiro Bimestre: '))
d = int(input('Quarto Bimestre: '))
while d > 10:
    d = int(input('Voce digitou uma nota maior que 10! Quarto Bimestre: '))

media = (a + b + c + d) / 4
print('A media final é {}'.format(media))


#EXEMPLO WHILE
# nota = int(input('Entre com uma nota: '))
# while nota > 10:
#     nota = int(input('Nota invalida. Entre com uma nota correta: '))



#Estrutura WHILE
# a = 0
# while a < 10:
#     print(a)
#     a += 1


#EXEMPLO FOR DENTRO DE FOR
# a = int(input('Entre com um valor: '))
# print('Sao numeros primos de 1 ate {}: ' .format(a))
# for num in range(a):
#     div = 0
#     for x in range(1, num+1):
#          resto = num % x
#          if resto == 0:
#              div += 1
#     if div == 2:
#         print(num)

#EXEMPLO FOR
# a = int(input('Entre com um numero: '))
#
# div = 0
# for x in range(1, a+1):
#      resto = a % x
#      if resto == 0:
#          div += 1
# if div == 2:
#     print('Numero {} é primo'.format(a))
# else:
#     print('Numero {} não é primo'.format(a))

#ESTRUTURA FOR
# for x in range(100):
#     print(x)

