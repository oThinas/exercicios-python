# range(número que começa, número máximo, incremento)
# range(start[0], stop, step[0])
numero = int(input('Digite o número para saber sua tabuada: '))
for i in range(11):
    print(numero, "x", i, "=", (numero * i))