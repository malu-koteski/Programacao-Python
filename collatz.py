num = int(input())

def collatz(num):
    if num == 1:
        return 0
    else:
        if num % 2 == 0:
            prox_num = num // 2
        else:
            prox_num = 3 * num + 1

        return 1 + collatz(prox_num)

quantid_passos = collatz(num)
print(quantid_passos)