# 1. Função (opcional/auxiliar) para estruturar os dados de um aluno antes de salvar
def adicionar_nota(RA, nota):
    # Retorna um dicionário simples com o RA e a nota informada
    return {"RA": RA, "nota": nota}


# 2. Lê o arquivo e usa eval() para transformar o texto em um dicionário Python
def ler_notas(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            # O eval() vai converter a string formatada de dicionário de volta para um objeto dict
            alunos = eval(conteudo)
            return alunos
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return {}
    except Exception as e:
        print(f"Erro ao ler ou processar o arquivo: {e}")
        return {}


# 3. Processa o dicionário de alunos e calcula a média de cada RA
def calcular_medias(alunos):
    medias = {}
    # 'alunos' deve ser um dicionário onde a chave é o RA e o valor é uma lista de notas
    for ra, notas in alunos.items():
        if notas:  # Garante que a lista de notas não está vazia
            medias[ra] = sum(notas) / len(notas)
        else:
            medias[ra] = 0.0
    return medias


# 4. Salva as médias calculadas em um novo arquivo de texto
def salvar_medias(medias, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write("RA,Média\n")  # Cabeçalho do arquivo
        for ra, media in medias.items():
            arquivo.write(f"{ra},{media:.2f}\n")
    print(f"Médias salvas com sucesso em '{nome_arquivo}'!")


# --- Exemplo Prático de Uso ---
if __name__ == "__main__":
    # Suponha que temos um arquivo chamado 'notas_alunos.txt' com o seguinte conteúdo de string:
    # {"RA001": [8.0, 7.5, 9.0], "RA002": [5.0, 6.0, 5.5], "RA003": [9.5, 10.0, 9.8]}

    # Criando o arquivo de teste localmente para demonstrar o funcionamento
    nome_arquivo_entrada = "notas_alunos.txt"
    dados_exemplo = '{"RA001": [8.0, 7.5, 9.0], "RA002": [5.0, 6.0, 5.5], "RA003": [9.5, 10.0, 9.8]}'

    with open(nome_arquivo_entrada, 'w', encoding='utf-8') as f:
        f.write(dados_exemplo)

    # Executando o fluxo do exercício:
    # 1. Ler as notas usando eval()
    dados_alunos = ler_notas(nome_arquivo_entrada)

    # 2. Calcular as médias
    lista_medias = calcular_medias(dados_alunos)

    # 3. Salvar os resultados em um novo arquivo
    salvar_medias(lista_medias, "medias_finais.txt")
