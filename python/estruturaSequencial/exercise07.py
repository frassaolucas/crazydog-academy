# Faca um Programa que calcule a area de um quadrado, em seguida mostre o dobro desta area para o usuario.

square_side = float(input('Informe o lado do quadrado: '))

square_area = square_side ** 2

print('A dobro da area do quadrado de lado ' + str(square_side) + ' e: ' + str(square_area * 2))