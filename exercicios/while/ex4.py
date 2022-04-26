# Crie um programa que peça letras como entrada, uma por vez, até que seja lida a letra ‘x’, ao final, o programa deve exibir a quantidade de letras lidas sem contabilizar ‘x’.
letras = []
while True:
    letra = input('Digite a letra: ')
    if letra == 'x':
        break
    letras.append(letra)
print('Número de letras:', len(letras))
        