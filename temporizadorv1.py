from winsound import PlaySound, SND_FILENAME
from time import sleep
tempo = 900
horas = 0
for t in range(1, tempo + 1):
    tempo -= 1
    minutos = tempo/60
    if minutos <= 60:
        print(f"Falta {horas} horas e {minutos:.2f} minutos")
    else:
        pass
    sleep(1)
PlaySound('tone1.wav', SND_FILENAME) * 3