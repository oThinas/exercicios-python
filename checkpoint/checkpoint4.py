# Linhas = semanas
# Colunas = dias

def criar_matriz(linhas, colunas):
  semanas = []
  for linha in range(linhas):
    dias = []
    for coluna in range(colunas):
      dias.append(int(input(f'Semana {linha + 1}, dia {coluna + 1} - Temperatura média: ')))
    semanas.append(dias)
  return semanas

def obter_n_cardinalidade():
  semanas = 0
  for semana in range(len(temperaturas)):
    dias = 0
    for dia in range(len(temperaturas[semana])):
      dias += 1
    semanas += 1
  return [semanas, dias]

def obter_menor_temperatura(matriz):
  menorTemperaturaDaSemana = []
  for semana in range(len(matriz)):
   menorTemperaturaDaSemana.append(min(matriz[semana]))
  return min(menorTemperaturaDaSemana)


def obter_lista_negativos(matriz):
  temperaturasNegativas = []
  for semana in range(len(matriz)):
    for dia in range(len(matriz[semana])):
      if matriz[semana][dia] < 0:
        temperaturasNegativas.append(matriz[semana][dia])
  return temperaturasNegativas

temperaturas = criar_matriz(
  int(input("Quantas semanas serão monitoradas?: ")), 
  int(input("Quantos dias, em cada semana, serão monitorados?: "))
)

semanasQuantidade = obter_n_cardinalidade()[0]
diasQuantidade = obter_n_cardinalidade()[1]

print(f'Sua matriz está com {semanasQuantidade} semanas que contém {diasQuantidade} {"dia" if diasQuantidade <= 1 else "dias"} cada.')

print(f'A menor temperatura é: {obter_menor_temperatura(temperaturas)}°C')

print(f'As temperaturas negativas são: {obter_lista_negativos(temperaturas)}')