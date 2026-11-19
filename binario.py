while True:
    print("1) Digite 1 para converter decimal para binário")
    print("2) Digite 2 para converter binário para decimal")
    print("3) Sair")

    opcao = input()

    #binario -> decimal
    if opcao ==  "2":

        binario = input()
        inverso = ""
        potencia = 0
        decimal = 0
        expoente = 0

        for numero in binario:
            inverso = str(numero) + inverso

        for digito in inverso:
            if digito == "1":
                decimal += 2 ** expoente
            expoente += 1

        print(decimal)

    #decimal -> binario
    elif opcao == "1":

        resto = ""
        decimal = input()
        decimal = int(decimal)
        inversoBinario = ""

        while decimal > 0:
            resto = decimal % 2
            inversoBinario = str(resto) + inversoBinario
            decimal = decimal // 2

        print(inversoBinario)

    elif opcao == "3":
        break

