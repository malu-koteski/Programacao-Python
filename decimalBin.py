num = int(input())

def conversao(num):
    if num < 2:
        return str(num)
    else:
        prox_decimal = num // 2
        resto = num % 2
        return conversao(prox_decimal) + str(resto)

conversao_decimal_binario = conversao(num)
print(conversao_decimal_binario)
