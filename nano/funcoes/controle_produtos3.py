def cadastrarProduto(lista):
    resposta = 'S'
    while resposta == 'S':
        equipamento = [input('Nome: '), float(input('Valor: ')), int(input('Serial: ')), input('Departamento: ')]
        lista.append(equipamento)
        resposta = input('Deseja continuar? (s/n) \n').upper()
        print('------------------')
        
def exibirProduto(lista):
    for item in lista:
        print('Nome:', item[0])
        print('Valor:', item[1])
        print('Serial:', item[2])
        print('Departamento:', item[3])
        print('------------------')
        
def buscarProduto(lista):
    nome = input('Digite o nome do equipamento para buscar: ')
    print('------------------')
    for item in lista:
        if nome == item[0]:
            print('Nome:', item[0])
            print('Valor:', item[1])
            print('Serial:', item[2])
            print('Departamento:', item[3])
            print('------------------')
            
def descontarProduto(lista, porc):
    nome = input('Digite o nome do elemento para descontar: ')
    print('------------------')
    for item in lista:
        if nome == item[0]:
            print('Valor antigo:', item[1])
            item[1] *= (porc / 100)
            print('Valor novo:', item[1])
            break
        
def excluirProduto(lista):
    serial = int(input('Digite o serial do equipamento danificado: '))
    print('------------------')
    for item in lista:
        if serial == item[2]:
            lista.remove(item)
            break
    

def exibirValores(lista):
    valores = []
    for item in lista:
        valores.append(item[1])
        
    # Exibe o valor dos itens
    if len(valores) > 0:
        print('O equipamento mais caro custa:', max(valores))
        print('O equipamento mais barato custa:', min(valores))
        print('O preço do inventário é de:', sum(valores))
        print('------------------')
        
def printLinha():
    print('-' * 40)