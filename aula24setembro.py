while True:
    valor = input()
    valores = valor.split()

    maior = float(valor[0])
    menor = float(valor[0])

    soma = 0
    inversa = ""
    isFirstTime = True

    for valor in valores:
        if valor.lower().strip() == 'sair':
            break
        numAtual = float(valor)
        if numAtual > maior:
            maior = numAtual
        if numAtual < menor:
            menor = numAtual

        soma = soma + numAtual


        if isFirstTime == True:
            inversa = str(numAtual)
            isFirstTime = False
        else:
            inversa = str(numAtual) + ", " + inversa


    print("Valor máximo: ", maior)
    print("Valor mínimo: ", menor)
    print("Soma dos elementos: ", soma)
    print("String em ordem inversa: ", inversa)

