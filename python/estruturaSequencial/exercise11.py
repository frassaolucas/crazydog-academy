# Faca um Programa que peca 2 numeros inteiros e um numero real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

number_one = int(input('Informe um numero inteiro: '))
number_two = int(input('Informe um outro numero inteiro: '))
number_three = float(input('Informe um numero real: '))

math_one = (number_one * 2) + (number_two / 2)
math_two = float((number_one * 3) + number_three)
math_three = number_three ** 3

print('O resultado do produto do dobro do primeiro com metade do segundo e: ' + str(math_one))
print('O resultado da soma do triplo do primeiro com o terceiro e: ' + str(math_two))
print('O resultado do terceiro elevado ao cubo e: ' + str(math_three))