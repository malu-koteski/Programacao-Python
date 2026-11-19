def ler_delimitadores():
    sequencia = []
    while True:
        entrada = input().strip()
        if entrada == "!":
            break
        elif entrada == "*":
            if len(sequencia) >= 2:
                sequencia.pop(-2)
        elif entrada in "([{)]}":
            sequencia.append(entrada)
    return sequencia

def verificar_balanceamento(sequencia):
    pilha = []
    pares = {")": "(", "]": "[", "}": "{"}

    for char in sequencia:
        if char in "([{":
            pilha.append(char)
        elif char in ")]}":
            if not pilha or pilha[-1] != pares[char]:
                return "mal formada"
            pilha.pop()
    return "bem formada" if not pilha else "mal formada"

delimitadores_finais = ler_delimitadores()
resultado = verificar_balanceamento(delimitadores_finais)
print(resultado)


