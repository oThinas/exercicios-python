# Crie  um  programa  que  solicite  ao  usuário  dois  números naturais  x  e  y,  o  programa  deverá  exibir  o  quociente  da divisão inteira de x por y sem usar os operadores de divisão e multiplicação. Por exemplo, se x=7 e y=2 a resposta será3,  pois  podemos  raciocinar  que  o  quociente  da  divisão inteira  de  x  por  yé  dado  pela  quantidade  de  vezes  que  y pode ser subtraídode x sem que x se torne negativo.
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
i = 0
while n2 <= n1:
    n1 -= n2
    i += 1
print(i)