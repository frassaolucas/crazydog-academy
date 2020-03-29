# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

def paycheck ():
  value_hour = float(input('Informe o valor (R$) que ganha por hora: '))
  worked_hours_month = float(input('Informe a quantidade de horas trabalhadas por mês: '))

  grossPay = float(value_hour * worked_hours_month)
  ir = float((grossPay * 11) / 100)
  inss = float((grossPay * 8) / 100)
  syndicate = float((grossPay * 5) / 100)
  netPay = float(grossPay - ir - inss - syndicate)

  print('Seu salário burto é: ' + str(grossPay) + '.')
  print('O desconto de IR é de: ' + str(ir) + '.')
  print('O desconto de INSS é de: ' + str(inss) + '.')
  print('O desconto do sindicato é de: ' + str(syndicate) + '.')
  print('Seu salário liquido é: ' + str(netPay) + '.')

paycheck()