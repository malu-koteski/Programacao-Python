num = int(input())

def soma_digitos(num):
    if num < 10:
        return num
    else:
        digito_final = num % 10
        resto = num // 10
        return digito_final + soma_digitos(resto)

def main():
    resultadoSoma = soma_digitos(num)
    print(resultadoSoma)

main()