# Faca um Programa que peca a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).

farenheit = float(input('Informe a temperatura em Farenheit: '))

celsius = (5 * (farenheit - 32) / 9)

print(str(farenheit) + ' graus Farenheit e equivalente a ' + str(celsius) + ' graus Celsius')