num_discos = int(input())

def torre_hanoi(num_discos, A_origem, B_aux, C_destino):
    if num_discos == 0:
        return ""
    else:
        torre_hanoi(num_discos - 1, A_origem, C_destino, B_aux)
        print(f"Mova o disco da torre {A_origem} para a torre {C_destino}.")
        torre_hanoi(num_discos - 1, B_aux, A_origem, C_destino)

quantidade_discos = torre_hanoi(num_discos, "A", "B", "C")

# void troca(int a, int b) {
#     int temp;
#     temp = a;
#     a = b;
#     b = temp;
# }
# int main (){
#     int a =5, b=10;
#     troca(a, b)
#     printf("%d" %d", a, b)
# } quais valores sao impressos, possivel p5 ou psub