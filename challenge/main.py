from funcoes import *
while True:
    # Menu Principal
    while True:
        cls()
        opcao = menuPrincipal()
        
        if opcao == 1:
            isCandidato = login()
            break
        
        if opcao == 2:
            cadastrarUsuario()
            
    # Menu Candidato ou Empresa
    if isCandidato:
        while True:
            cls()
            opcao = menuCandidato(isCandidato)
            
            if opcao == 1:
                atualizarPerfil(isCandidato)
            
            if opcao == 2:
                candidatar()
                
            if opcao == 3:
                break
    elif not isCandidato and isCandidato != None:
        while True:
            cls()
            opcao = menuEmpresa(isCandidato)
            
            if opcao == 1:
                atualizarPerfil(isCandidato)
            
            if opcao == 2:
                cadastrarVaga(input("Código da Vaga: "))
                
            if opcao == 3:
                break