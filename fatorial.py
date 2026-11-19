num = int(input())

def fatorial(num):
    if num == 0:
        return 1
    else:
        anterior = fatorial(num - 1)
        return anterior * num

def main():
    resultado = fatorial(num)
    print(resultado)

main()