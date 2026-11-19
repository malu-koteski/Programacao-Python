def verificar(simbolos, indice, i):
    if indice == len(simbolos):
        return len(i) == 0

    simbolo = simbolos[indice]
    pares = {")": "(", "]": "[", "}": "{"}

    if simbolo in ("(", "[", "{"):
        i.append(simbolo)
        return verificar(simbolos, indice + 1, i)
    elif simbolo in pares:
        if not i or i[-1] != pares[simbolo]:
            return False
        i.pop()
        return verificar(simbolos, indice + 1, i)
    return verificar(simbolos, indice + 1, i)

resultados = []

while True:
    linha = input().strip()

    if linha.upper() == "SAIR":
        break

    simbolos = []

    for caractere in linha:
        if caractere == "!":
            break

        if caractere == "*":
            if len(simbolos) >= 2:
                simbolos.pop(-2)
        elif caractere in ("(",")", "[","]", "{", "}"):
            simbolos.append(caractere)

    if verificar (simbolos, 0, []):
        resultados.append("bem formada")
    else:
        resultados.append("mal formada")

    for resposta in resultados:
        print(resposta)