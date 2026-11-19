#Exercício 1: Cálculo de Área de um Retângulo
#Escreva um código em Python que solicite ao usuário a largura e a altura de um retângulo e calcule a área desse
#retângulo. Em seguida, exiba o resultado na tela.

base = float(input("Digite a base do retangulo: "))
altura = float(input("Digite a altura do retangulo: "))

if (base and altura) > 0:
    area = base * altura
    print("A area eh:", area)
else:
    print("Insira um valor valido para base e altura.")

#Exercício 2: Conversão de Temperatura
#Crie um programa que converta uma temperatura em graus Celsius para Fahrenheit. O programa deve receber a
#temperatura em Celsius como entrada do usuário e exibir a temperatura equivalente em Fahrenheit.

celsius = int(input("Digite a temperatura enm graus Celsius: "))
fahrenheit = (9 * celsius + 160) / 5

print("A temperatura em  Farenheit eh: ", fahrenheit, "graus.")

#Exercício 3: Calculadora de IMC (Índice de Massa Corporal)
#Desenvolva um programa que calcule o IMC de uma pessoa. O usuário deve fornecer o peso (em quilogramas) e a
#altura (em metros). O programa deve calcular o IMC e exibir na tela.

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

if (altura and peso) > 0:
    imc = peso / altura ** 2
    print("O seu imc eh: ", imc)
else:
    print("Insira um valor valido para peso e altura.")

#Exercício 4: Calculadora de Desconto em Compras
#Crie um programa que simule uma calculadora de desconto em compras. O usuário deve inserir o preço original do
#produto e o percentual de desconto a ser aplicado. O programa deve calcular o valor final após o desconto e exibir
#na tela.

valorProduto = float(input("Insira o valor  original do produto comprado: "))
desconto = float(input("Insira o valor percentual de desconto: "))

valorPago = valorProduto - ((desconto * valorProduto) / 100)

print("O valor pago pelo produto com desconto foi: ", valorPago)

#Exercício 5: Troca de Horas e Minutos
#Crie um programa que permita ao usuário inserir uma quantidade de minutos e converta essa quantidade em horas
#e minutos. O programa deve fazer a conversão usando a divisão inteira e o operador de resto da divisão (módulo),
#sem o uso de condicionais. Em seguida, o programa deve exibir o resultado na forma "X horas e Y minutos".

#Por exemplo, se o usuário inserir 150 minutos, o programa deve exibir "2 horas e 30 minutos".

#Dica: Use a divisão inteira para calcular as horas e o operador de resto da divisão para calcular os minutos
#restantes.

minutos = int(input("Insira a quantidade de minutos: "))

horas = minutos // 60
minutosHora = minutos % 60

print(horas, "horas e", minutosHora, "minutos").;

#1: Imprimir na tela seu nome e cidade de nascimento.

print("Maria Luisa Koteski Bustamante de Melo")
print("Sao Jose dos Campos")

#2. Quando queremos imprimir algo diferente de uma sequência de caracteres (texto),
#não usamos aspas.
#Verifique o que ocorre se executarmos o seguinte comando:
print (3 * 4 * 5)
#Usando a mesma lógica, imprima na tela a quantidade de segundos em um mês.

print(24 * 3600 * 30)

#3. A função print também pode imprimir conteúdos de variáveis. Execute o exemplo
#abaixo e veja o que aparece na tela:
idade = 20
profissao = "estudante"
print (idade)
print (profissao)
#Tente executar um exemplo similar com outros valores de variáveis de sua escolha.
#Lembre-se de que a escolha do nome das variáveis é importante para que o código seja
#compreensível.

termo = 4
curso = "Engenharia da Computacao"
print(termo)
print(curso)

#4. A função print nos permite concatenar (juntar) texto a outras informações, como
#valores numéricos. Para isso, é preciso usar a vírgula (,) para separar cada entrada de
#dados. Execute o exemplo abaixo:
x = 10
y = 5
s = x + y
print ("A soma é", s)
#Repare que a vírgula está concatenando (juntando) o texto e o valor da variável s.

#5. A função input é usada em Python para entrada de dados. Execute o exemplo abaixo:
nome = input ("Digite seu nome: ")
print ("Ola, ", nome)

# 6. Qual o tipo (dentre int, float e str) você utilizaria para guardar as seguintes
# opções:
# a. Seu nome;
nome = str(input("Digite seu nome completo: "))
# b. O dia de hoje;
dia = int(input("Digite o dia de hoje: "))
# c. Sua idade;
idade = int(input("Digite sua idade: "))
# d. A média de notas da turma;
media = float(input("Digite sua media: "))
# e. Quantas casas há em Campinas
numCasas = int(input("Digite o numero de casas em Campinas: "))

# 7. Use o operador // para divisão inteira e % para resto da divisão inteira. Por exemplo:
print (44 // 3)
print (44 % 3)
# Agora use estes operadores para calcular quantas dúzias de ovos temos em 403 ovos e
# quantos ovos restam.

ovos = 403
duzias = ovos // 12
ovosRestantes = ovos % 12

print(duzias, "duzias", ovosRestantes, "ovos")

# 8. Assim como normalmente vemos na matemática, na computação também temos os
# operadores lógicos, como igualdade, diferença, maior, menor etc. Quando fazemos uma
# comparação lógica e guardamos o resultado em uma variável, aquela variável vai
# receber um valor cujo tipo é chamado de booleano, que assume os valores verdadeiro
# ou falso. Por exemplo:
a = 10
b = 5
c = a < b
print(c)
# O que aparece na tela?
print("Aparece 'falso' visto que a eh maior que b")

# 9. Um cuidado que devemos ter é com o operador de igualdade. Não confundir com o
# operador de atribuição =. O operador de igualdade é == (duplo igual). Por
# exemplo:
a = 2
b = 3
c = a = b
print(c)
# Qual será a saída?
print("A saida eh b, ou seja 3, porque estamos atribuindo o valor de b a c")

# Como queremos uma saída verdadeira (True) ou falsa (False), e não um número, a
# operação na terceira linha deveria ser c = a == b. Rode novamente o código a seguir
# e veja a saída.
a = 2
b = 3
c = a == b
print(c)
print("A saida eh booleana agora, porque estamos atribuindo para c a comparacao de se a eh igual a b, ou seja eh falso")

# 10. Vamos executar um exemplo similar ao do exercício anterior, agora com o
# operador da diferença, !=. Os comandos abaixo geram qual saída?
a = 2
b = 3
c = a != b
print(c)
# Outros operadores lógicos que você pode testar são o de de (maior), >= (maior ou
# igual), <= (menor ou igual).

print("Gera uma saida booleana, para o caso inicial, 'true'")

# 11. Use os operadores aritméticos + para adição, - para subtração, / para divisão e
# * para multiplicação. Observe quais saídas são geradas pelos seguintes comandos:
print (10 + 5)
print("Gera 15")

print (3 - 12)
print("Gera -9")

print (4 + 2 * 3)
print("Gera 10")

print (12 / 4)
print("Gera 3.0")

print (12 / 5)
print("Gera 2.4")

# 12. O operador aritmético ** é usado em Python para calcular potências
# (exponenciação). Qual será a saída do comando abaixo?
print (2 ** 5)
print("A saida eh 32")
# Usando esse operador, escreva um programa que imprima na tela todas as
# potências no intervalo [2, 10] para um número de entrada n entre [2 a 9].

numero = int(input("Digite um numero entre 2 a 9: "))

for i in range(2, 10):
    potencia = numero ** i
    print(potencia)

# 13. Outros operadores lógicos em Python são and (‘E’) e or (‘OU’). Eles são
# usados, por exemplo, para fazer comparações compostas - o que veremos em mais
# detalhes na próxima seção e no decorrer do curso. Por enquanto, observe a saída gerada
# pelos comandos abaixo.
a = 10
b = 20
c = a == b
d = a != b
print (c)
print (d)
print (c and d)
print (c or d)

# 14. Considere as seguintes expressões lógicas: A e B. Determine se as expressões A e
# B são equivalentes, com base em sua estrutura lógica:
A: (P or Q) and (not R)
B: (P and not R) or (Q and not R)
# Dica: Pode mostrar se os resultados das tabelas de verdade de A e B são iguais.

print("Ver imagem anexada com a resolucao")