# Crie um programa que leia um número natural n dado pelo usuário e exiba sóos n primeiros pares a partir de 0. Por exemplo, se n=6 ser exibido 0 2 4 6 8 10
n = int(input('Digite um número: '))
i = 0
while i < n:
    print(2 * i)
    i += 1