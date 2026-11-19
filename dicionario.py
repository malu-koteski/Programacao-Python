notasAlunos = {}

while True:
    nome = input()

    if nome.upper() == "FIM":
        break

    nota = float(input())
    notasAlunos[nome] = nota

somaNotas = sum(notasAlunos.values())
totalAlunos = len(notasAlunos)
mediaTurma = somaNotas / totalAlunos

print(f"Média da turma: {mediaTurma: .2f}")

aprovados = []

for nome, nota in list(notasAlunos.items()): # for posicao em elemento
    if nota >= mediaTurma:
        aprovados.append(nome)

print("Alunos aprovados:", ", ".join(aprovados))