with open('nano\manipular_arquivo\economic-indicators.csv', 'r') as file:
  internationalFlightsIn2014 = 0
  highPassengerCount = 0
  highHotelAvgDailyRate = 0.0
  
  userYearPassenger = input('Qual ano você deseja verificar a quantidade total de passageiros?\nAno: ')
  userYearHotel = input('Em qual ano você deseja verificar o mês da maior média diária de um hotel?\nAno: ')
  
  for line in file.readlines()[1: -1]:
    class Constants:
      YEAR = line.split(',')[0]
      MONTH = line.split(',')[1]
      PASSENGER = float(line.split(',')[2])
      INTERNATIONAL_FLIGHTS = float(line.split(',')[3])
      HOTEL_AVG_DAILY_RATE = float(line.split(',')[5])
    
    constant = Constants()
    
    if constant.YEAR == '2014':
      internationalFlightsIn2014 += constant.INTERNATIONAL_FLIGHTS
    
    if constant.PASSENGER > highPassengerCount:
      highPassengerCount = constant.PASSENGER
      highPassengerYear = constant.YEAR
      highPassengerMonth = constant.MONTH
    
    if line.split(',')[0] == userYearPassenger:
      highPassengerCount += constant.PASSENGER
      
    if line.split(',')[0] == userYearHotel and float(line.split(',')[5]) > highHotelAvgDailyRate:
      highHotelAvgDailyRate = constant.HOTEL_AVG_DAILY_RATE
      highHotelAvgDailyRateMonth = constant.MONTH
      

print('- Qual o total de voos internacionais que partiram do aeroporto de Logan no ano de 2014?')
print(f'Resposta: {internationalFlightsIn2014:.0f}')

print('- Quando (mês e ano) ocorreu o maior trânsito de passageiros no aeroporto de Logan?')
print(f'Resposta: {highPassengerMonth}/{highPassengerYear}')

print('- Qual o total de passageiros que passaram pelo aeroporto de Logan, no ano que for específicado pelo usuário?')
print(f'Resposta: No ano de {userYearPassenger}, voaram {highPassengerCount:.0f} passageiros')

print('- Qual o mês que possui a maior média de diária de um hotel, com base no ano especificado pelo usuário?')
print(f'Resposta: No ano de {userYearHotel}, o mês com a maior média diária em um hotel foi o mês {highHotelAvgDailyRateMonth}')