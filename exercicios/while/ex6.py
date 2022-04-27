# Crie um programa que receba como entrada o crédito e depois o preço de itens comprados por  esse  cliente.  O  programa  deverá  parar de solicitar novos preços quando o crédito disponível for insuficiente para pagar por um deles. Ao final exiba o total da compra e o crédito restante.
i = 0
precoTotal = 0
credito = float(input('Crédito disponível: '))
compra = True
while compra:
    if precoTotal == credito:
        break
    else:
        i += 1
        precoUnitario = float(input(f'Preço do item {i}: '))
        if precoUnitario != -1:
            if precoUnitario <= credito and precoTotal + precoUnitario <= credito:
                precoTotal += precoUnitario
            else:
                i -= 1
                print('-------------------------------------')
                print('Limite excedido, item não adicionado.')
                print(f'Crédito restante: R${credito - precoTotal:.2f}')
                print('-------------------------------------')
        else:
            compra = False
print('-------------------------------------')
print("Limite atingido. Terminando compra...") if precoTotal == credito else print("Terminando compra...")
print(f'Preço total: R${precoTotal:.2f}')
credito -= precoTotal
print(f'Crédito restante: R${credito:.2f}')
print('-------------------------------------')