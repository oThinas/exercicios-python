salarios = [0, 0, 0, 0]
soma = 0
i = 1

while i <= len(salarios):
    salarios[i] = float(input('Salário: R$'))
    soma += salarios[i]
    i += i
media = soma / len(salarios)

i = 0
while i< len(salarios):
    if salarios[i] < media:
        print(f'Abaixo da média: R${salarios[i]:.2f}')
    i += 1