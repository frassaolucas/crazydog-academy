#  Faca um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

def painting():
  area_to_paint = float(input('Informe a área a ser pintada (em metros quadrados): '))
  paint_cans_value = 80
  paint_cans = 0

  if area_to_paint % 54 == 0:
    paint_cans = int(area_to_paint / 54)
  else:
    paint_cans = int((area_to_paint / 54) + 1)

  total_price = paint_cans * paint_cans_value

  print('Para pintar ' + str(area_to_paint) + ' metros quadrados deve-se utilizar ' + str(paint_cans) + ' latas de tinta, no valor de R$' + str(paint_cans_value) + ' por lata, em um total de R$' + str(total_price) + '.')

painting()