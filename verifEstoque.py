while True:
    estoque = input().lower().split()
    produtosCliente = input().split()
    produtosFaltando = []

    if "sair" in estoque:
        break

    for item in produtosCliente:
        if item not in estoque:
            produtosFaltando.append(item)

    if len(produtosFaltando) == 0:
        print("Tudo em estoque!")
    else:
        print("Faltam os itens:", produtosFaltando)

#versao sem while

produtoEstoque = input().lower().split()
produtoCliente = input().lower().split()
produtoFaltando = []

for item in produtoCliente:
    if item not in produtoEstoque:
        produtoFaltando.append(item)

if len(produtoFaltando) == 0:
    print("Tudo em estoque!")
else:
    print(f"Faltam os itens:{produtoFaltando}")






