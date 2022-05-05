from time import sleep
import os

clear = lambda: os.system('cls')
horaAlarme = int(input("Hora: "))
minutoAlarme = int(input("Minuto: "))
segundoAlarme = int(input("Segundo: "))

hora = 0
while hora < 24:
    minuto = 0
    while minuto < 60:
        segundo = 0
        while segundo < 60:
            print(f'{hora:02}:{minuto:02}:{segundo:02}')
            sleep(1)
            clear()
            if hora == horaAlarme and minuto == minutoAlarme and segundo == segundoAlarme:
                print("BIP-BIP")
                break
            segundo += 1
        if hora == horaAlarme and minuto == minutoAlarme and segundo == segundoAlarme:
            break 
        minuto += 1
    if hora == horaAlarme and minuto == minutoAlarme and segundo == segundoAlarme:
        break
    hora += 1
print("Dia encerrado.")
