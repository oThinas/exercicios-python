print('CALCULE A MÉDIA...')
n1 = float(input('Número 1 = '))
n2 = float(input('Número 2 = '))
falta = int(input('Faltas = '))
media = (n1 + n2) / 2
if media >= 6 and falta < 18:
    situacao = 'APROVADO'
else:
    situacao = 'REPROVADO'

print('Sua média é', media, 'e você está', situacao)
#modificação teste