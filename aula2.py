#Operadores Aritiméticos
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado =('Soma: {soma} '
      '\nSubtração: {subtracao} '
      '\nMultiplicação: {multiplicacao} '
      '\nDivisão: {divisao} '
      '\nResto: {resto}' .format(soma=soma,
                            subtracao=subtracao,
                            multiplicacao=multiplicacao,
                            divisao=divisao,
                            resto=resto))
print(resultado)
# print('Soma: ' + str(soma))
# print ('Subtração: ' + str(subtracao))
# print('Multiplicação: ' +str(multiplicacao))
# print('Divisão: ' +str(divisao))
# print('Resto de divisão: ' + str(resto))