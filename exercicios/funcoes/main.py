# Constant
DOUBLE = 2

def handleInput():
  return int(input('Número: '))

def handleCalculateDouble(number):
  return number * DOUBLE

def handleShowResult(result):
  print(f'Resultado: {result}')

# number = handleInput()
# result = handleCalculateDouble(number)
# handleShowResult(result)

handleShowResult(handleCalculateDouble(handleInput()))