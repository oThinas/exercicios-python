with open('nano\manipular_arquivo\economic-indicators.csv', 'r') as file:
  flightsIn2014 = 0
  highPassengerCount = 0
  highHotelAvgDailyRate = 0.0
  
  userYearPassenger = input('Qual ano você deseja verificar a quantidade total de passageiros?\nAno: ')
  userYearHotel = input('Em qual ano você deseja verificar o mês da maior média diária de um hotel?\nAno: ')
  
  for line in file.readlines()[1: -1]:
    if line.split(',')[0] == '2014':
      flightsIn2014 += float(line.split(',')[3])
    
    if float(line.split(',')[2]) > highPassengerCount:
      highPassengerCount = float(line.split(',')[2])
      highPassengerYear = line.split(',')[0]
      highPassengerMonth = line.split(',')[1]
    
    if line.split(',')[0] == userYearPassenger:
      highPassengerCount += float(line.split(',')[2])
      
    if line.split(',')[0] == userYearHotel and float(line.split(',')[5]) > highHotelAvgDailyRate:
      highHotelAvgDailyRate = float(line.split(',')[5])
      highHotelAvgDailyRateMonth = line.split(',')[1]
      

print('- Qual o total de voos internacionais que partiram do aeroporto de Logan no ano de 2014?')
print(f'Resposta: {flightsIn2014:.0f}')

print('- Quando (mês e ano) ocorreu o maior trânsito de passageiros no aeroporto de Logan?')
print(f'Resposta: {highPassengerMonth}/{highPassengerYear}')

print('- Qual o total de passageiros que passaram pelo aeroporto de Logan, no ano que for específicado pelo usuário?')
print(f'Resposta: No ano de {userYearPassenger}, voaram {highPassengerCount:.0f} passageiros')

print('- Qual o mês que possui a maior média de diária de um hotel, com base no ano especificado pelo usuário?')
print(f'Resposta: No ano de {userYearHotel}, o mês com a maior média diária em um hotel foi o mês {highHotelAvgDailyRateMonth}')