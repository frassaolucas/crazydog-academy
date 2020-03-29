# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte formula: (72.7*altura) - 58

height = float(input('Informe sua altura em metros: '))

ideal_weight = (72.7 * height) - 58

print('Seu peso e: ' + str(ideal_weight))