from time import sleep
from winsound import PlaySound, SND_FILENAME
tempo = float(input("Digite quantos minutos você quer:"))
tempoconvert = tempo * 60
horas = tempoconvert // 3600
minutos = (tempoconvert % 3600) // 60
segundos = tempoconvert % 60

for t in range(1, int(tempoconvert)):
	tempoconvert -= 1
	print(f"Faltam {int(horas):02d} horas, {int(minutos):02d} minutos e {int(segundos):02d} segundos")
	sleep(1)
PlaySound('tone1', SND_FILENAME)