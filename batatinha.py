
def transformar(frase, i):
    if i == len(frase):
        return ""

    letra = frase[i]

    if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u":
        return "1" + transformar(frase, i + 1)
    elif letra == " ":
        return "-" + transformar(frase, i + 1)
    else:
        return letra + transformar(frase, i + 1)

def ler_frases(n):
    if n == 0:
        return
    frase = input()
    if "batatinha" in frase.lower():
        print("Bingo!")
        return

    print(transformar(frase, 0))
    ler_frases(n - 1)

n = int(input())
ler_frases(n)
