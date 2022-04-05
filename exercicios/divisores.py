num = int(input('Digite um número inteiro para descobrir seus divisores possíveis: '))
i = 1
print('Os divisores de', num, 'são:')
while i <= num:
    if num % i == 0:
        print(num, "/", i, "=", num / i)
    i += 1