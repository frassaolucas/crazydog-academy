# Faca um Programa que peca as 4 notas bimestrais e mostre a media.

nota_um = float(input('Informe a primeira nota: '))
nota_dois = float(input('Informe a segunda nota: '))
nota_tres = float(input('Informe a terceira nota: '))
nota_quatro = float(input('Informe a quarta nota: '))

media = (nota_um + nota_dois + nota_tres + nota_quatro) / 4

print('A media e: ' + str(media))