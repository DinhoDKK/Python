#Estruturas condicionais e operadores lógicos
a = int(input('Primeiro Bimestre: '))
if a > 10:
    a = int(input('Voce digitou uma nota maior que 10! Primeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
if b > 10:
    b = int(input('Voce digitou uma nota maior que 10! Segundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
if c > 10:
    c = int(input('Voce digitou uma nota maior que 10! Terceiro Bimestre: '))
d = int(input('Quarto Bimestre: '))
if d > 10:
    d = int(input('Voce digitou uma nota maior que 10! Quarto Bimestre: '))

media = (a + b + c + d) / 4
print('A media final é {}'.format(media))

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('A media final é {}'.format(media))
# else:
#     print('Foi digitado um valor superior a 10')
print('Programa finalizado.')


# a = int(input('Digite o primeiro valor: '))
# b = int(input('Digite o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or resto_b == 0:
#     print('Foi digitado um numero par')
# else:
#     print('nenhum numero par foi digitado')
# print('Programa finalizado.')



# a = int(input('Digite o primeiro valor: '))
# b = int(input('Digite o segundo valor: '))
# c = int(input('Digite o terceiro valor: '))
#
# if a > b and a > c:
#     print('O maior valor é: {}' .format(a))
# elif b > a and b > c:
#     print('O maior valor é {}' .format(b))
# else:
#     print('O maior valor é {}'.format(c))
# print('Programa finalizado.')