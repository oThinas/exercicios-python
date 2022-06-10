# Com o "with open... as ..." não é necessário chamar a função "close()", além de conseguir dar um "alias" para o arquivo com o "as"
local = 'D:/Programacao/Desenvolvimento/Python/exercicios-python/nano/arquivos/'

with open(f'{local}teste.txt', 'w') as arquivo:
  arquivo.write('Nunca foi tão fácil criar um arquivo.\n')

with open(f'{local}teste.txt', 'a') as arquivo:
  arquivo.write('Continuação do texto.')