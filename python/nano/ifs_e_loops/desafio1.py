# O módulo solicitará um nível de acesso de uma pessoa que pode ser: ADM, USER ou GUEST e o gênero dessa pessoa.
# Caso o nível seja ADM, a mensagem exibida deverá ser "Olá administrador" ou "Olá administradora", dependendo do gênero da pessoa. "Olá usuário(a)" para USER, seguindo a mesma lógica acima. "Olá visitante" para GUEST. "Olá desconhecido" para qualquer outro nível diferente de ADM, USER e GUEST. Considere apenas os gêneros masculino e feminino

nivel = input('Qual seu nível de acesso? (adm/user/guest): ').upper()
if nivel == 'GUEST':
    print('Olá, visitante')
else:
    genero = input('Qual seu gênero? ').upper()
    if genero.startswith('FEM') and nivel == 'ADM':
        print('Olá, administradora')
    elif genero.startswith('FEM') and nivel == 'USER':
        print('Olá, usuária')
    elif nivel == 'ADM':
        print('Olá, administrador')
    elif nivel == 'USER':
        print('Olá, usuário')
    elif genero.startswith('FEM'):
        print('Olá, desconhecida')
    else:
        print('Olá, desconhecido')