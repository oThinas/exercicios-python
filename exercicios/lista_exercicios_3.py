import math

# 1. Fazer uma função que tem como parâmetro de entrada três números inteiros a, b, c e fornece como saída o menor dentre os três números.
def findSmallestNumber(a, b, c):
  return min(a, b, c)

# 2. Fazer uma função que tem como parâmetro de entrada três números inteiros a, b, c e fornece como saída o maior dentre os três números.
def findBigestNumber(a, b, c):
  return max(a, b, c)

# 3. Fazer uma função que tem como parâmetro de entrada um número inteiro positivo n e fornece como saída a soma de todos os números inteiros menores ou iguais a n.
def sumAllSmallerNumbers(n):
  sum = 0
  for number in range(n + 1):
    sum += number
  return sum
    
# 4. Fazer uma função que tem como parâmetro de entrada um número inteiro positivo n e fornece como saída o fatorial desse número.
def factorial(n):
  times = 1
  for number in range(1, n + 1):
    times *= number
  return times

# 5. Fazer um programa que lê um número inteiro positivo n e imprime a divisão do produto dos n primeiros  números  positivos  pela  soma  dos  n  primeiros  números  positivos.  Usar  as  funções elaboradas nos exercícios 3 e 4.
def divideFactorialPerSum(n):
  return (factorial(n)) / (sumAllSmallerNumbers(n))

# 6. Fazer uma função que tem como parâmetros de entrada três números reais a, b, c e fornece como saída a maior raiz da equação do 2º grau: 
# ax² + bx + c = 0
# Se não houver raízes reais, a função deve retornar o número −1. 
def quadratic(a, b, c):
  if b * b - 4 * a * c < 0: #Delta negativo
    return -1
  x1 = (b * (- 1) + math.sqrt(b * b - 4 * a * c)) / (2 * a)
  x2 = (b * (- 1) - math.sqrt(b * b - 4 * a * c)) / (2 * a)
  return [x1, x2]

# 7. Fazer  um  programa  que  imprime  a  soma  das  maiores  raízes  de  três  equações  de  2º  grau  com entradas  fornecidas  pelo  usuário.  O  programa  deve  utilizar  a  função  elaborada  no  exercício anterior.  Caso  a  equação  não  tenha  raízes  reais,  o  programa  deve  somar  0  no  lugar  da  maior raiz.
def sumBiggestQuadraticResult():
  print("Equação 1")
  a1 = float(input("a: "))
  b1 = float(input("b: "))
  c1 = float(input("c: "))
  print("Equação 2")
  a2 = float(input("a: "))
  b2 = float(input("b: "))
  c2 = float(input("c: "))
  print("Equação 3")
  a3 = float(input("a: "))
  b3 = float(input("b: "))
  c3 = float(input("c: "))
  x1 = quadratic(a1, b1, c1)
  x2 = quadratic(a2, b2, c2)
  x3 = quadratic(a3, b3, c3)
  
  if x1 == -1:
    x1 = [0, 0]
  if x2 == -1:
    x2 = [0, 0]
  if x3 == -1:
    x3 = [0, 0]
  
  return max(x1[0], x1[1]) + max(x2[0], x2[1]) + max(x3[0], x3[1])

# 8. Modificar  a  função  do  exercício  6  da  seguinte  forma:  além  dos  parâmetros  de  entrada  reais a,b,c,  um  quarto  parâmetro  deve  ser  adicionado,  o  qual  será  responsável  para  decidir  se  a saída  da  função  vai  ser  a  maior  ou  a  menor  raiz  (incluir  o  caso  de  raízes  iguais  com  a  maior raiz). Novamente, se não houver raízes reais, a função deve retornar o número −1.
def newQuadratic(a, b, c, option: 'small' or 'big'):
  x = quadratic(a, b, c)
  if x == -1:
    x = [-1, -1]
    
  if option == 'small':
    return min(x[0], x[1])
  elif option == 'big':
    return max(x[0], x[1])

# 9. Faça uma função que recebe por parâmetro o raio (R) de uma esfera e calcula o seu volume, onde o volume é dado por: v = (4/3).π.R³.
def calculateVolume(r):
  return (4 / 3) * math.pi * r ** 3

# 10. Faça  uma  função  que  recebe  por  parâmetro  um  valor  inteiro  e  positivo  e  retorna  Verdadeiro caso o valor seja primo, e Falso, caso contrário.
def checkPrimeNumber(prime):
  if prime > 1:
    for target in range(2, prime):
      if prime % target == 0:
        return False # Não é primo
    return True # É primo
  return False # Não é primo
  
# 11. Faça  uma  função  que  recebe  a  idade  de  uma  pessoa  em  anos,  meses  e  dias  e  retorna  essa idade expressa em dias.
def ageInDays(y, m, d):
  d += y * 365
  d += m * 30
  return d

# 12. Faça  uma  função  que  recebe  a  idade  de  um  nadador  por  parâmetro  e  retorna,  também  por parâmetro, a categoria desse nadador de acordo com a tabela abaixo:
#            Idade               | Categoria
#          5 a 7 anos            | Infantil A
#         8 a 10 anos            | Infantil B
#         11 a 13 anos           | Juvenil A
#         14 a 17 anos           | Juvenil B
# Maiores de 18 anos (inclusive) | Adulto
def categorizeSwimmer(age):
  if age < 5:
    return 'Idade menor que 5 anos não é permitida'
  elif age >= 5 and age <= 7:
    return 'Infantil A'
  elif age >= 8 and age <= 10:
    return 'Infantil B'
  elif age >= 11 and age <= 13:
    return 'Juvenil A'
  elif age >= 14 and age <= 17:
    return 'Juvenil B'
  else:
    return 'Adulto'

# 13. Faça  uma  função  que  recebe  a  média  final  de  um  aluno  por  parãmetro  e  retorna  o  seu conceito, conforme a tabela abaixo:
#      Nota     | Conceito
#  de 0.0 a 4.9 |    D
#  de 5.0 a 6.9 |    C
#  de 7.0 a 8.9 |    B
# de 9.0 a 10.0 |    A
def score(average):
  if average >= 0 and average <= 4.9:
    return 'D'
  elif average >= 5 and average <= 6.9:
    return 'C'
  elif average >= 7 and average <= 8.9:
    return 'B'
  elif average >= 9 and average <= 10.0:
    return 'A'

# 14. Faça uma função que recebe, por parâmetro, a altura (alt) e o sexo de uma pessoa, e retorna o seu  peso  ideal.  Para  homens,  calcular  o  peso  ideal  usando  a  fórmula:  P  =  72,7.alt  -  58.  Para mulheres, utilize a fórmula: P = 62,1.alt – 44,7.
def idealWeight(height, gender: 'male' or 'female'):
  if gender == 'male':
    return 72.7 * height - 58
  elif gender == 'female':
    return 62.1 * height - 44.7
  else:
    return 'Gênero não esperado'

# 15. A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes, coletando dados sobre o salário  e  número  de  filhos.  Faça  uma  função  que  leia  esses  dados  para  um  número  não determinado  de  pessoas  e  retorne  a  média  de  salário  da  população,  a  média  do  número  de filhos, o maior salário e o percentual de pessoas com salário até R$350,00.
def cityAverage(salaries, sons):
  salaryAverage = sum(salaries) / len(salaries)
  sonAverage = sum(sons) / len(sons)
  salaryBiggest = max(salaries)
  
  salaryLessThan350Count = 0
  for salary in salaries:
    if salary <= 350:
      salaryLessThan350Count += 1
  
  return [salaryAverage, sonAverage, salaryBiggest, salaryLessThan350Count]

# 16. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.
def foundDividers(number):
  dividers = [0]
  for previousNumber in range(1, number + 1):
    if number % previousNumber == 0:
      dividers.append(previousNumber)
  return dividers
    
# 17. Escreva uma função que recebe, por parâmetro, dois valores X e Z e calcula e retorna XZ (sem utilizar funções ou operadores de potência prontos).
def functionPow(x, z):
  result = 1
  i = 0
  while i < z:
    result *= x
    i += 1
  return result