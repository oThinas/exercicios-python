base = float(input('Base: '))
while base <= 0:
    print('A base não pode possuir um valor negativo ou igual a 0')
    base = float(input('Base: '))

altura = float(input('Altura: '))
while altura <= 0:
    print('A altura não pode possuir um valor negativo ou igual a 0')
    altura = float(input('Altura: '))
    
area = (base * altura) / 2
print('Área:', area)