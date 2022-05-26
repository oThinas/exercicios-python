votos = []
votosTotal = 0
votosPorcentagem = []
sistemaOperacional = ["Windows Server: ", "Unix: ", "Linux: ", "Netware: ", "macOS: ", "Outros: "]

print("Digite a quantidade de votos da equete")

for i in sistemaOperacional:
  aux = int(input(i))
  votos.append(aux)
  votosTotal += aux

for i in range(len(votos)):
  aux = (100 * votos[i]) / votosTotal
  votosPorcentagem.append(aux)
  
print("Sistema operacional | Votos | %")
for i in range(len(votos)):
  print(f'{sistemaOperacional[i]} | {votos[i]} | {votosPorcentagem[i]:.1f}')
print("Total: ", votosTotal)


aux = votos.index(max(votos))
print(f'O Sistema Operacional mais votado foi o {sistemaOperacional[aux]} com {max(votos)} votos, correspondendo a {max(votosPorcentagem)}% dos votos')