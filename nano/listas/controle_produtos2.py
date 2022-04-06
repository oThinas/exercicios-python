inventario = []

# Adicionar itens ao inventário
resposta = 'S'
while resposta == 'S':
    equipamento = [input('Nome: '), float(input('Valor: ')), int(input('Serial: ')), input('Departamento: ')]
    inventario.append(equipamento)
    resposta = input('Deseja continuar? (s/n) \n').upper()
    print('------------------')

# Exibe todos os equipamentos
for i in inventario:
    print('Nome:', i[0])
    print('Valor:', i[1])
    print('Serial:', i[2])
    print('Departamento:', i[3])
    print('------------------')
    
# Exibe o registro do elemento buscado pelo nome
nome = input('Digite o nome do equipamento para buscar: ')
print('------------------')
for i in inventario:
    if nome == i[0]:
        print('Nome:', i[0])
        print('Valor:', i[1])
        print('Serial:', i[2])
        print('Departamento:', i[3])
        print('------------------')
        
# Desconta 10% do valor no registro do elemento buscado pelo nome
nome = input('Digite o nome do elemento para descontar: ')
print('------------------')
for i in inventario:
    if nome == i[0]:
        i[1] *= 0.9
        break

# Deleta o registro do elemento buscado pelo serial
serial = int(input('Digite o serial do equipamento danificado: '))
print('------------------')
for i in inventario:
    if serial == i[2]:
        inventario.remove(i)
        break

# Exibe a lista atualizada de equipamentos
for i in inventario:
    print('Nome:', i[0])
    print('Valor:', i[1])
    print('Serial:', i[2])
    print('Departamento:', i[3])
    print('------------------')
    
# Listas numéricas
valores = []
for i in inventario:
    valores.append(i[1])
    if len(valores) > 0:
        print('O equipamento mais caro custa:', max(valores))
        print('O equipamento mais barato custa:', min(valores))
        print('O preço do inventário é de:', sum(valores))