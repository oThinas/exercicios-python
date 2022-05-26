import os
os.system('cls' if os.name=='nt' else 'clear')

votos = []
votosTotal = 0
votosPorcentagem = []
sistemaOperacional = ["Windows Server", "Unix", "Linux", "Netware", "macOS", "Outros"]

print("Digite a quantidade de votos da enquete")

for i in sistemaOperacional:
  aux = int(input(f'{i}: '))
  votos.append(aux)
  votosTotal += aux

for i in range(len(votos)):
  aux = (100 * votos[i]) / votosTotal
  votosPorcentagem.append(aux)
  
print("Resultado da Enquete:")
print("Sistema operacional | Votos | Porcentagem")
for i in range(len(votos)):
  espacosNome = " " * (len("Sistema operacinal |") - len(sistemaOperacional[i]))
  espacosVoto = " " * (len("Votos ") - len(str(votos[i])))
  print(f'{sistemaOperacional[i]}{espacosNome}| {votos[i]}{espacosVoto}| {round(votosPorcentagem[i])}%')
print(f'Total: {votosTotal}')


aux = votos.index(max(votos))
print(f'O Sistema Operacional mais votado foi o {sistemaOperacional[aux]} com {max(votos)} votos, correspondendo a {round(max(votosPorcentagem))}% dos votos')