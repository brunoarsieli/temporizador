from winsound import PlaySound, SND_FILENAME
from time import sleep
tempo = int(input("Deseja que o alarme toque depois de quantos minutos? "))*60
horas = 0
for t in range(1, tempo + 1):
    tempo -= 1
    print(tempo)
    sleep(1)
while tempo == 0:
    PlaySound('tone1.wav', SND_FILENAME)
    sleep(1)