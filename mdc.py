X, Y = map(int, input().split())

def retorna_mdc(X, Y):
    if Y == 0:
        return X
    else:
        resto = X % Y
        return retorna_mdc(Y, resto)

mdc_calculado = retorna_mdc(X, Y)
print(mdc_calculado)