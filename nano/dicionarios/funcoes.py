def perguntar():
    opcao = input('O que deseja realizar?' + 
              '\n(i) - Inserir ou atualizar um usuário' + 
              '\n(p) - Pesquisar um usuário' + 
              '\n(e) - Excluir um usuário' +
              '\n(l) - Listar usuários' +
              '\n(0) - Sair\n').lower()
    print('---------------')
    return opcao

def inserir(usuarios):
    chave = input('Login: ')
    usuarios[chave] = [input('Nome: '), 
                            input('Última data de acesso: '), 
                            input('Última estação acessada: ')]
    print('Cadastrado com sucesso')
    print('---------------')
    
def pesquisar(usuarios, chave):
    if usuarios.get(chave) != None:
        # print(usuarios.get(chave)) # Exibe todos os elementos da chave
        print('Nome:', usuarios.get(chave)[0],
              '\nÚltimo acesso no dia:', usuarios.get(chave)[1],
              '\nÚltima estação acessada:', usuarios.get(chave)[2]) #Exibe elementos individuiais do dicionário
        print('---------------')
    else:
        print('Login inexistente. Tente novamente')
        print('---------------')
    
def excluir(usuarios, chave):
    if usuarios.get(chave) != None:
        print('Usuário:', chave, '\nNome:', usuarios.get(chave)[0], '\nÚltimo acesso no dia:', usuarios.get(chave)[1], '\nÚltima estação acessada:', usuarios.get(chave)[2])
        print('Excluído com sucesso')
        print('---------------')
        del usuarios[chave]
    else:
        print('Login inexistente. Tente novamente')
        print('---------------')
        
def listar(usuarios):
    print('Listando...')
    print('---------------')
    for chave, dadosUsuario in usuarios.items():
        # print('Login:', chave, '= Nome:', usuarios.get(chave)[0], 'Último acesso no dia:', usuarios.get(chave)[1], 'Última estação acessada:', usuarios.get(chave)[2]) # Não funciona, porque o método items() retorna: ['Enrico Flores', '03/06/2017', 'RaioX02'].
        print('Login:', chave, '=', dadosUsuario)
        print('---------------')