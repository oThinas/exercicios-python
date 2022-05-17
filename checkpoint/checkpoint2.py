# Ex1: Calculadora  
controle = True
numero1 = int(input("Digite o número 1: "))

while controle:
    operacao = input("+ Adição | - Subtração | * Multiplicação | / Divisão\n")
    numero2 = int(input("Digite o número 2: "))
    
    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "*":
        resultado = numero1 * numero2
    elif operacao == "/":
        resultado = numero1 / numero2
    else:
        print("Operação inválida.")
    
    if numero1 >= numero2:
        print("Maior =", numero1, "\nMenor =", numero2, "\nResultado =", resultado)
    else:
        print("Maior =", numero2, "\nMenor =", numero1, "\nResultado =", resultado)
        
    numero1 = resultado
    
    opcao = int(input("Deseja fazer mais alguma operação? (1 - Sim | 2 - Não)\n"))
    if opcao == 2:
        controle = False

# Ex 2: Login e Senha
controle = True
loginCerto = "Moranguete"
senhaCerta = "123456"
erros = 0

while controle:
    loginUsuario = input("Usuário: ")
    senhaUsuario = input("Senha: ")
    
    #Acertou o login
    if loginUsuario == loginCerto:
        #Acertou a senha
        if senhaUsuario == senhaCerta:
            print("Login efetuado com sucesso.")
            break;
        #Errou a senha
        else:
            erros += 1
            print("Login ou senha inválidos")
    #Errou o login
    else:
        erros += 1
        print("Login ou senha inválidos")
        
    #Redefinir quando errar 3 vezes
    if erros == 3:
        print("Redefina as inforamações de login")
        loginUsuario = input("Usuário: ")
        loginCerto = loginUsuario
        senhaUsuario = input("Senha: ")
        senhaCerta = senhaUsuario
        print("Login e senha redefinidos")
        
# Ex 3: Tabuada
numero = int(input("Digite o número que quer saber a tabuada: "))
multiplicacao = 1

while multiplicacao <= 10:
    resultado = numero * multiplicacao
    print(numero, "x", multiplicacao, "=", resultado)
    multiplicacao += 1
