# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

# def painting():
#   area_to_paint = float(input('Informe o valor, em metros quadrados, da área a ser pintada: '))
#   area_painted_per_liter = 6.0
#   painting_can_volume = 18.0
#   painting_can_price = 80.0
#   painting_gallon_volume = 3.6
#   painting_gallon_price = 25.0

#   painting_cost(area_to_paint, area_painted_per_liter, painting_can_volume, painting_can_price, 'lata(s)')
#   painting_cost(area_to_paint, area_painted_per_liter, painting_gallon_volume, painting_gallon_price, 'galão(ões)')
#   # painting_cans_gallons()

# def painting_cost(area, efficiency, volume, price, container):
#   total_container = 0

#   if area % (efficiency * volume) == 0:
#     total_container = int(area / (efficiency * volume))
#   else:
#     total_container = int((area / (efficiency * volume)) + 1)

#   total_price = total_container * price

#   print('Para se pintar uma área de ' + str(area) + ' metros quadrados será necessário ' + str(total_container) + ' ' + container + ' de tinta, cada uma custando R$' + str(price) + ', com um total de R$' + str(total_price))

def painting_cans_gallons(area, efficiency, can_volume, can_price, gallon_volume, gallon_price):
  total_cans = 0
  total_gallons = 0
  total_cans_price = 0
  total_area_per_can = efficiency * can_volume

  if area % (total_area_per_can) == 0: # Check if it's possible to use whole cans to paint the desired area
    total_cans = int(area / (total_area_per_can))
  else:
    total_cans = int((area / (total_area_per_can)) + 1)
    total_gallons = int(((area % can_volume) / gallon_volume) + 1)

    if total_gallons * gallon_price > can_price: # Check which is cheaper
      total_cans += 1
      total_gallons = 0
      total_cans_price = total_cans * can_price
  
  print(total_cans)
  print(total_gallons)
    

# painting()
painting_cans_gallons(18, 6.0, 18.0, 80.0, 3.6, 25.0)