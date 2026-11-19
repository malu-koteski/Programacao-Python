frase = input().strip()
inversa = ""
for letra in frase:
    inversa = str(letra) + inversa
if frase == inversa:
    print("A cadeia é palíndromo.")
else:
    print("A cadeia não é palíndromo.")