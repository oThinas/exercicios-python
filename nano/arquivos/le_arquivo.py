local = 'D:/Programacao/Desenvolvimento/Python/exercicios-python/nano/arquivos/'

with open(f'{local}teste.txt', 'r') as arquivo:
  conteudo = arquivo.readlines()

print('Tipo de dado da variável', type(conteudo))
print('Conteúdo do arquivo:', conteudo)