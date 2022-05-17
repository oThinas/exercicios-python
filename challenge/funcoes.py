import os

# candidatos[Login] = {[Senha, Nome completo, Email, CPF, Cidade, Telefone]}
candidatos = {}
# empresas[Login] = {[Senha, Nome, CNPJ, Cidade, Telefone, Porte, Número de Vagas Abertas]}
empresas = {}
# vagas[Id] = {[Título, Salário Mínumo, Salário Máximo, Descrição, Cidade]}
vagas = {}


# Exibe o Menu principal
def menuPrincipal():
    logo()
    opcao = int(input("[1] - Login | [2] - Cadastro\n"))
    cls()
    return opcao

# Exibe o Menu do Candidato
def menuCandidato(isCandidato):
    logo()
    print("Tipo de conta:", ("Candidato" if isCandidato else "Empresa"))
    opcao = int(input("[1] - Atualizar Perfil | [2] - Se Candidatar | [3] - Logout\n"))
    cls()
    return opcao

# Exibe o Menu da Empresa
def menuEmpresa(isCandidato):
    logo()
    print("Tipo de conta:", ("Candidato" if isCandidato else "Empresa"))
    opcao = int(input("[1] - Atualizar Perfil | [2] - Cadastrar/Atualizar Vaga | [3] - Logout\n"))
    cls()
    return opcao

# Cadastra usuários
def cadastrarUsuario():
    opcao = int(input("Criar conta como: [1] - Candidato | [2] - Empresa\n"))
    cls()
    
    # Cadastra Candidatos
    if opcao == 1:
        isCandidato = True
        chave = input("Login: ")
        # Se o Login não existir
        if candidatos.get(chave) == None:
            candidatos[chave] = [input("Senha: "),
                                input("Nome completo: "),
                                input("Email: "),
                                input("CPF: "),
                                input("Cidade: "),
                                input("Telefone: ")]
            input("Cadastro feito com sucesso!")
        else:
            print("Login existente. Tente novamente")
            linha()
            input("Pressione Enter para continuar: ")
    
    # Cadastra Empresas
    elif opcao == 2:
        isCandidato = False
        chave = input("Login: ")
        # Se o Login não existir
        if empresas.get(chave) == None:
            empresas[chave] = [input("Senha: "),
                            input("Nome: "),
                            input("CNPJ: "),
                            input("Cidade: "),
                            input("Telefone: "),
                            input("Porte ([P] - Pequeno | [M] - Médio | [G] - Grande): ").upper(),
                            0]
            # Garante que o porte vai ser P, M ou G
            if empresas.get(chave)[5] != "P" and empresas.get(chave)[5] != "M" and empresas.get(chave)[5] != "G":
                porteEmpresa = empresas.get(chave)[5]
                while porteEmpresa != "P" and porteEmpresa != "M" and porteEmpresa != "G":
                    porteEmpresa = input("Porte ([P] - Pequeno | [M] - Médio | [G] - Grande): ").upper()
                empresas[chave] = [empresas.get(chave)[0],
                                empresas.get(chave)[1],
                                empresas.get(chave)[2],
                                empresas.get(chave)[3],
                                empresas.get(chave)[4],
                                porteEmpresa,
                                empresas.get(chave)[6],]
            input("Cadastro feito com sucesso!")
        else:
            print("Login existente. Tente novamente!")
            linha()
            input("Pressione Enter para continuar: ")

# Login
def login():
    opcao = "S"
    while opcao == "S":
        chave = input("Login: ")
        senha = input("Senha: ")
        if candidatos.get(chave) != None and senha == candidatos.get(chave)[0]:
            return True # isCandidato = True
        elif empresas.get(chave) != None and senha == empresas.get(chave)[0]:
            return False # isCandidato = False
        else:
            opcao = ""
            while opcao != "S" and opcao != "N":
                opcao = input("Login ou senha inválidos! Tentar novamente? ([S] - Sim | [N] - Não)\n").upper()
    cls()


# Atualiza perfil
def atualizarPerfil(isCandidato):
    opcao = "S"
    while opcao == "S":
        chave = input("Login: ")
        senha = input("Senha: ")
        if empresas.get(chave) != None or candidatos.get(chave) != None:
            if senha == empresas.get(chave)[0] or senha == candidatos.get(chave)[0]:
                if isCandidato:
                    print("Acesso concedido!")
                    linha()
                    candidatos[chave] = [input("Senha: "),
                                        input("Nome completo: "),
                                        input("Email: "),
                                        input("CPF: "),
                                        input("Cidade: "),
                                        input("Telefone: ")]
                    input("Atualizado com sucesso!")
                    break
                else:
                    print("Acesso concedido!")
                    linha()
                    empresas[chave] = [input("Senha: "),
                                    input("Nome: "),
                                    input("CNPJ: "),
                                    input("Cidade: "),
                                    input("Telefone: "),
                                    input("Porte ([P] - Pequeno | [M] - Médio | [G] - Grande): ").upper(),
                                    0]
                    # Garante que o porte vai ser P, M ou G
                    if empresas.get(chave)[5] != "P" and empresas.get(chave)[5] != "M" and empresas.get(chave)[5] != "G":
                        porteEmpresa = empresas.get(chave)[5]
                        while porteEmpresa != "P" and porteEmpresa != "M" and porteEmpresa != "G":
                            porteEmpresa = input("Porte ([P] - Pequeno | [M] - Médio | [G] - Grande): ").upper()
                        empresas[chave] = [empresas.get(chave)[0],
                                        empresas.get(chave)[1],
                                        empresas.get(chave)[2],
                                        empresas.get(chave)[3],
                                        empresas.get(chave)[4],
                                        porteEmpresa,
                                        empresas.get(chave)[6],]
                    input("Atualizado com sucesso!")
                    break
            else:
                opcao = ""
                while opcao != "S" and opcao != "N":
                    opcao = input("Login ou senha inválidos! Tentar novamente? ([S] - Sim | [N] - Não)\n").upper()
        else:
            input("Login ou senha inválidos! Voltando para o menu...")
            break
         
    
def cadastrarVaga(chave):
    vagas[chave] = [input("Título: "),
                    input("Salário mínimo: "),
                    input("Salário máximo: "),
                    input("Descrição: "), 
                    input("Cidade: ")]
    print("Cadastro/Atualização feita com sucesso!")
    
def candidatar():
    for chave, dadosVaga in vagas.items():
        print("Código da Vaga:", chave, "=", dadosVaga)
    opcao = ""
    while opcao != "S" and opcao != "N":
        opcao = input("Deseja se candidatar para alguma vaga? ([S] - Sim | [N] - Não)\n").upper()
        if opcao == "S":
            chave = input("Código da Vaga: ")
            if vagas.get(chave) != None:
                input("Concluído. Boa sorte!")
            else:
                input("Digite um Código de Vaga válido.")
    
# Limpa o console
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Exibe o logo
def logo():
    print(("-" * 8) + " TECH INSIDE " + ("-" * 8))

# Cria uma linha
def linha():
    print("-" * 29)