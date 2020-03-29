# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a 
# velocidade de um link de Internet (em Mbps), calcule e informe o tempo 
# aproximado de download do arquivo usando este link (em minutos).

def download_file():
  file_size = float(input('Informe o tamanho do arquivo para download (em MBs): '))
  download_speed = float(input('Informe a velocidade de download do link de internet (em MBs): '))

  download_eta = (file_size / download_speed) / 60

  print('O tempo aproximado para término do download é de: ' + str(download_eta) + ' minutos')  

download_file()