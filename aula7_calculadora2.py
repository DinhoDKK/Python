#FUNÇÕES METODOS  E CLASSES

class Calculadora:

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
print(calculadora.soma(2, 10))
print(calculadora.subtracao(5, 3))
print(calculadora.multiplicacao(10, 5))
print(calculadora.divisao(100, 2))