# Faca um Programa que pergunte quanto voce ganha por hora e o numero de horas trabalhadas no mes. Calcule e mostre o total do seu salario no referido mes.

hours_value = float(input('Informe o valor que ganha por hora: '))
hours_month = float(input('Informe o numero de horas trabalho por mes: '))

total_value = hours_value * hours_month

print('O total do salario e: ' + str(total_value))