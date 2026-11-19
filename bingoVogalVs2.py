numero = int(input())
resultados = []

for i in range(numero):
    frase = input()
    if "batatinha" in frase.lower():
        resultados.append("Bingo!")
        break
    else:
        fraseTrocada = frase
        vogais = "aeiouAEIOU"

        for vogal in vogais:
            fraseTrocada = fraseTrocada.replace(vogal, "1")

        fraseTrocada = fraseTrocada.replace(" ", "-")
        resultados.append(fraseTrocada)

for resposta in resultados:
    print(resposta)

