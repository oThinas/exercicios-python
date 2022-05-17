# Crie  um  programa  que  receba  como entrada os preços de itens comprados em um  supermercado  por  um  cliente,  ao final, o programa deverá exibir o total da  compra.  Para  informar  que  não  há mais itens a serem comprados, o cliente deve digitar o valor -1.
i = 0
precoTotal = 0
while True:
    i += 1
    precoUnitario = float(input(f'Preço do item {i}: '))
    if precoUnitario == -1:
        break
    precoTotal += precoUnitario
print(f'Preço total do carrinho: R${precoTotal:.2f}')