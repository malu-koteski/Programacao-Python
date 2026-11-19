while True:
    print("a) obter o elemento com valor máximo;")
    print("b) obter o elemento com valor mínimo;")
    print("c) obter a soma de todos os elementos;")
    print("d)  imprimir os elementos em ordem inversa.")
    print("e) sair, o programa deve terminar indicando 'fim'")

    opcao = input().strip()

    if opcao == "e":
        print("fim")
        break

    numero = input().split()

    if not numero:
        continue

    valorMaximo = float(numero[0])
    valorMinimo = float(numero[0])

    soma = 0
    inverso = ""

    for valor in numero:
        numAtual = float(valor)

        if numAtual > valorMaximo:
            valorMaximo = numAtual

        if numAtual < valorMinimo:
            valorMinimo = numAtual

        soma = soma + numAtual

        inverso = str(numAtual) + ", " + inverso

    if opcao == "a":
            print(f"Valor máximo: {valorMaximo}")
    elif opcao == "b":
        print(f"Valor mínimo: {valorMinimo}")
    elif opcao == "c":
        print(f"Soma dos elementos: {soma}")
    elif opcao == "d":
        print(f"String em ordem inversa: {inverso}")
    print()



while True:
    frase = input().replace(" ", "").strip().lower()
    invertida = ""

    if frase == "sair":
        print("fim")
        break

    for letra in frase:
        invertida = str(letra) + invertida

    if frase == invertida:
        print("A cadeia é palíndromo.")
    else:
        print("A cadeia não é palíndromo.")



while True:
    frase = input().replace(" ", "").strip().lower()
    invertida = frase[::-1]

    if frase == "sair":
        print("fim")
        break

    if frase == invertida:
        print("A cadeia é palíndromo.")
    else:
        print("A cadeia não é palíndromo.")


while True:
    print("1) Digite 1 para converter decimal para binário")
    print("2) Digite 2 para converter binário para decimal")
    print("3) Sair")

    opcao = input()

    if opcao == "1":
        numDecimal = input()
        numDecimal = int(numDecimal)
        inversoBinario = ""
        resto = ""

        while numDecimal > 0:
            resto = numDecimal % 2
            inversoBinario = str(resto) + inversoBinario
            numDecimal = numDecimal // 2

        print(inversoBinario)

    elif opcao == "2":
        numBinario = input().strip()
        decimal = 0

        for digito in numBinario:
            decimal = (decimal * 2) + int(digito)

        print(f"Resultado: {decimal}"  )

    elif opcao == "sair":
        print("fim")
        break

