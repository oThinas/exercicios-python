local = 'D:/Programacao/Desenvolvimento/Python/exercicios-python/nano/arquivos/'

with open(f'{local}index.html', 'w') as index:
  index.write('<!DOCTYPE html>\n')
  index.write('<html lang="pt-br" dir="ltr">\n')
  index.write('<head>\n')
  index.write('<title>Document</title>\n')
  index.write('</head>\n')
  index.write('<body>\n')
  index.write('<h2>Nomes importantes para o projeto:</h2>\n')
  
  nome=''
  while nome != 'SAIR':
    nome = input('Digite um nome ou SAIR: ').upper()
    if nome != 'SAIR':
      index.write(f'<p>{nome}</p>\n')
  
  index.write('</body>\n')
  index.write('</html>')