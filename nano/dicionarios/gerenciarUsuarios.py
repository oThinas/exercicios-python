# Inicie perguntando ao usuário o que ele deseja realizar: inserir, pesquisar, excluir, listar ou sair.
from funcoes import *

usuarios = {}
opcao = 'i'

while opcao == 'i' or opcao == 'p' or opcao == 'e' or opcao == 'l':
    opcao = perguntar()
    
    if opcao == 'i':
        inserir(usuarios)

    if opcao == 'p':
        pesquisar(usuarios, input('Login: '))
        
    if opcao == 'e':
        excluir(usuarios, input('Login: '))
    
    if opcao == 'l':
        listar(usuarios)
    
    if opcao == '0':
        print('Encerrando sistema...')
        break