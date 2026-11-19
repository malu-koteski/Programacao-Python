numerosPares = []
numerosImpares = []
paresTransformados = []

while True:
    entrada = input()

    if entrada == "sair":
        break

    numeros = int(entrada)

    if numeros % 2 == 0:
        numerosPares.append(numeros)
        paresTransformados.append(numeros * 2)

    if numeros % 2 != 0:
        numerosImpares.append(numeros)

print("Pares transformados:", paresTransformados)
print("Ímpares originais:", numerosImpares)

numerosImpares = [] #versao sem while q n for pedido
numerosTransformados = []

entrada = int(input())

for i in range(entrada):
    numero = int(input())

    if numero % 2 == 0:
        numerosTransformados.append(numero * 2)
    else:
        numerosImpares.append(numero)

print(f"Pares transformados: {numerosTransformados}")
print(f"Ímpares originais: {numerosImpares}")