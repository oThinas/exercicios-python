def printElements(lista):
  for index, element in enumerate(lista):
    print(f'Elemento {index}: {element}')
    
def checkListLength(lista):
  return len(lista)

def createList(numberOfElements):
  for element in range(numberOfElements):
    aux = input('Digite o elemento a ser inserido: ')
    if (aux.isnumeric()):
      aux = int(aux)
    createdLista.append(aux)
  
    
createdLista = []
createList(int(input('Digite quantos elementos a lista vai ter: \n')))
print(f'Tamanho da lista: {checkListLength(createdLista)}')
printElements(createdLista)