resposta = 'SIM'
while resposta == 'SIM':
    nome = input('Nome do paciente: ')
    idade = int(input('Idade do paciente: '))
    doencaContagiosa = input('Suspeita de doença infecto-contagiosa? ').upper()
    
    while doencaContagiosa != 'SIM' and doencaContagiosa != 'NAO':
        print('Por favor, digite sim ou nao')
        doencaContagiosa = input('Suspeita de doença infecto-contagiosa? ').upper()

    # Encaminhar para sala
    if doencaContagiosa == 'SIM':
        print('Sala AMARELA')
    else:
        print('Sala BRANCA')
        
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
    resposta = input('Gostaria de verificar outro paciente? ').upper()