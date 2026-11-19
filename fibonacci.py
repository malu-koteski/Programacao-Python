dicionario_fibonacci = {1: 1, 2: 1}

def fibonacci(n):
    if n in dicionario_fibonacci:
        return dicionario_fibonacci[n]

    if n == 1 or n == 2:
        return 1

    dicionario_fibonacci[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return dicionario_fibonacci[n]

resposta = []

while True:
    entrada = input().strip()

    if entrada.upper() == "SAIR":
        break

    numero = int(entrada)

    if numero % 2 != 0:
        resultado = fibonacci(numero)
        resposta.append(f"{numero} - FIBONACCI: {resultado}")

for linha in resposta:
    print(linha)