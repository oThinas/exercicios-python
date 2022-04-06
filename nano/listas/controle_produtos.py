equipamentos = []
valores = []
seriais = []
departamentos = []

# Adicionar elementos à lista
resposta = 'S'
while resposta == 'S':
    equipamentos.append(input('Equipamento: '))
    valores.append(float(input('Valor: ')))
    seriais.append(int(input('Número Serial: ')))
    departamentos.append(input('Departamento: '))
    
    resposta = input('Deseja continuar? (s/n) \n').upper()
    print('------------------')
    
# Percorrer os elementos da lista
for i in range(len(equipamentos)):
    print('Nome:', equipamentos[i])
    print('Valor:', valores[i])
    print('Serial:', seriais[i])
    print('Departmaneto:', departamentos[i])
    print('------------------')
    
# Exibe um elemento em específico buscado pelo nome
busca = input('Digite o nome do equipamento que deseja buscar: ')
print('------------------')
for i in range(len(equipamentos)):
    if busca == equipamentos[i]:
        print('Nome:', equipamentos[i])
        print('Valor:', valores[i])
        print('Serial:', seriais[i])
        print('Departmaneto:', departamentos[i])
        print('------------------')

# Dá um desconto de 10% em um elemento em específico buscado pelo nome
desconto = input('Digite o nome equipamento que será descontado: ')
print('------------------')
for i in range(len(equipamentos)):
    if desconto == equipamentos[i]:
        valores[i] *= 0.9
        break

# Deleta do registro um elemento em específico buscado pelo serial
deletado = int(input('Digite o serial do equipamento danificado: '))
print('------------------')
for i in range(len(equipamentos)):
    if deletado == seriais[i]:
        del equipamentos[i]
        del valores[i]
        del seriais[i]
        del departamentos[i]
        break

# Exibe a lista atualizada de equipamentos
for i in range(len(equipamentos)):
    print('Nome:', equipamentos[i])
    print('Valor:', valores[i])
    print('Serial:', seriais[i])
    print('Departamento:', departamentos[i])
    print('------------------')