numero = int(input())

resultados = []

for i in range(numero):
    frase = input()
    if "batatinha" in frase.lower():
        resultados.append("Bingo!")
        break
    else:
        fraseTrocada = frase.replace("a", "1").replace("e", "1").replace("i", "1").replace("o", "1").replace("u", "1")
        fraseTrocada = fraseTrocada.replace("A", "1").replace("E", "1").replace("I", "1").replace("O", "1").replace("U", "1")
        fraseTrocada = fraseTrocada.replace(" ", "-")
        resultados.append(fraseTrocada)

for resposta in resultados:
    print(resposta)

