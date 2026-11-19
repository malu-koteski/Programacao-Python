valoresLista = []
primo = []

while True:
    numero = input()

    if numero.upper() == "SAIR":
        break

    valor = numero.split()

    for valores in valor:
        valoresLista = int(valores)
        numPrimo = True

        if valoresLista < 2:
            numPrimo = False

        else:
            for i in range(2, int(valoresLista ** 0.5) + 1):
                if valoresLista % i == 0:
                    numPrimo = False
                    break

        if numPrimo:
            primo.append(valoresLista)
            print(valoresLista, "PRIMO")