notaUm = float(input('Informe a primeira nota: '))
notaDois = float(input('Informe a segunda nota: '))

def calcula_media(valorUm, valorDois):
  media = str((valorUm + valorDois) / 2)
  print('A media eh ' + media)

calcula_media(notaUm, notaDois)