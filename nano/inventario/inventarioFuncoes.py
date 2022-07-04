inventario = {}
local = 'D:/Programacao/Desenvolvimento/Python/exercicios-python/nano/inventario/'

def exibirMenu():
  op = 0
  while op not in range(1, 4):
    op = int(input("[1] - Registrar ativo | [2] - Salvar registros | [3] - Exibir ativos\n"))
    return op
  
def registrarItem():
  op = 'S'
  while op == 'S':
    inventario[input('Número do patrimonial: ')] = [input('Data da última atualização: '),
                                                    input('Descrição: '),
                                                    input('Departamento: ')]
    op = input('Digite [s] para mais itens.\n').upper()
    
def incluirItem():
  if verificarInventarioVazio():
    return
  
  with open(f'{local}inventario.csv', 'a') as documento:
    for chave, valor in inventario.items():
      documento.write(f'{chave};{valor[0]};{valor[1]};{valor[2]}\n')
      print('Incluídos com sucesso!')
      
def exibirItem():
  try: 
    with open(f'{local}inventario.csv', 'r') as documento:
      for linha in documento:
        lista = linha.split(';')
        print(
          f'Data: {lista[1]}\nDescrição: {lista[2]}\nDepartamento: {lista[3]}'
        )
  except IOError:
    print('Arquivo não existe.')