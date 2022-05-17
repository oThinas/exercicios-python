# Ex 1: Criar um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15%  de  comissão  sobre  suas  vendas  efetuadas,  calcular  e  imprimir  o  total  a receber no final do mês.

vendedor = input('Nome do vendedor: ')
salarioFixo = float(input('Salário fixo: '))
totalVendas = float(input('Vendas no mês: (em reais) '))

salario = salarioFixo + (0.15 * totalVendas)
print('Salário:', salario)

# Ex 2: Criar  um  algoritmo  que  leia  o  salário  de  um  funcionário  e  calcule  o  imposto  de renda (IR) a ser pago a partir do salário do funcionário. Se o salário for menor que R$  1.257,12  está  isento  do  imposto.  Se  o  salário  for  entre  R$  1.257,12  e  R$ 2.510,00  (inclusive),  a  alíquota  do  imposto  é  17%.  Se  o  salário  for  superior  a  R$ 2.510,00, a alíquota do imposto é 28%. Apresentar na tela o salário bruto, o salário líquido e o valor do imposto.

salario = float(input('Salário bruto: '))
if 1257.12 <= salario and salario <= 2510:
    imposto = salario * 0.17
elif salario > 2510:
    imposto = salario * 0.28
else:
    imposto = 0

print('Salário bruto:', salario)
print('Salário líquido:', (salario - imposto))
print('Imposto:', imposto)

#Ex 3:  Criar um algoritmo que leia a idade de um nadador e apresenta na tela a sua categoria seguindo as regras:
# Infantil A = 5 - 7 anos
# Infantil B = 8 - 10 anos
# Juvenil A = 11 - 13 anos
# Juvenil B = 14 - 17 anos
# Sênior = +18 anos

idade = int(input('Idade do nadador: '))
if 5 <= idade and idade <= 7:
    print('Categoria: Infatil A')
elif 8 <= idade and idade <= 10:
    print('Categoria: Infatil B')
elif 11 <= idade and idade <= 13:
    print('Categoria: Juvenil A')
elif 14 <= idade and idade <= 17:
    print('Categoria: Juvenil B')
elif idade >= 18:
    print('Categoria: Sênior')
else:
    print('Nenhuma categoria')