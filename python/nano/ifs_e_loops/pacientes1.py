nome = input('Nome do paciente: ')
idade = int(input('Idade do paciente: '))
doencaContagiosa = input('Suspeita de doença infecto-contagiosa? ').upper()
    
# Encaminhar para sala
if doencaContagiosa == 'SIM':
    print('Sala AMARELA')
elif doencaContagiosa == 'NAO':
    print('Sala BRANCA')
else:
    print('Dados inseridos incorretamente, reinicie o sistema')
    
# Fila com prioridade ou sem prioridade
if idade >= 65:
    print('COM PRIORIDADE')
else:
    genero = input('Gênero do paciente: ').upper()
    if genero.startswith('FEM') and idade > 10:
        gravidez = input('A paciente está grávida? ').upper()
        if gravidez == 'SIM':
            print('COM PRIORIDADE')
        else:
            print('sem prioridade')
    else:
        print('sem prioridade')