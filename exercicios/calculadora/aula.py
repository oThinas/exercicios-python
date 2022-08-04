def somar(numero1, numero2):
  return numero1 + numero2

def subtrair(numero1, numero2):
  return numero1 - numero2

def multiplicar(numero1, numero2):
  return numero1 * numero2

def dividir(numero1, numero2):
  return numero1 / numero2

def exibirMenu():
  while True:
    print('CALCULADORA\n')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão\n')
    opcao = int(input(': '))
    if opcao in range(1, 5):
      break
  return opcao

def exibirResultado(resultado):
  print(f'Resultado: {resultado}')
  
def inserirDados():
  numero = int(input('Número: '))
  return numero

def controlador(numero1, numero2, opcao):
  if opcao == 1:
    return somar(numero1, numero2)
  
  elif opcao == 2:
    return subtrair(numero1, numero2)
    
  elif opcao == 3:
    return multiplicar(numero1, numero2)
    
  else:
    return dividir(numero1, numero2)