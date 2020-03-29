# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

gender = input('Informe o seu sexo (masculino ou feminino): ')
height = float(input('Informe a sua altura (em metros): '))

if gender.lower() == 'masculino':
  male_ideal_weight = (72.7 * height) - 58
  print('O seu peso ideal e ' + str(male_ideal_weight) + 'kg')
elif gender.lower() == 'feminino':
  female_ideal_weight = (62.1 * height) - 44.7
  print('O seu peso ideal e ' + str(female_ideal_weight) + 'kg')
else:
  print('Não possível identificar o seu sexo')