# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

fishes_weight = float(input('Informe o peso total de peixes pescados (em quilos): '))
limit_weight = 50

if fishes_weight > limit_weight:
  overweight = fishes_weight - limit_weight
  fine_bill = overweight * 4

  print('A quantidade pescada de ' + str(fishes_weight) + 'kg ultrapassou em ' + str(overweight) + 'kg o limite permitido de ' + str(limit_weight) + 'kg, resultando em multa de R$' + str(fine_bill) + '.')
else:
  print('A quantidade pescada de ' + str(fishes_weight) + 'kg não ultrapassou o limite de ' + str(limit_weight) + 'kg.')