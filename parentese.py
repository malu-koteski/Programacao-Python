opc = []

while True:
    entrada = input().strip()
    if entrada == "!":
        break

    elif entrada == "*":
        if len(opc) >= 2:
            opc.pop(-2)

    elif entrada in "([{)]}":
        opc.append(entrada)

    texto = "".join(opc)

    while "()" in texto or "[]" in texto or "{}" in texto:
        texto = texto.replace("()", "")
        texto = texto.replace("[]", "")
        texto = texto.replace("{}", "")

if texto == "":
    print("bem formada")
else:
    print("mal formada")
