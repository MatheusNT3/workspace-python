# print("Hello, World!") # print é o comando para exibir algo na tela

# Váriaveis sao espaços na memória que guardam valores
# Imput é o comando para receber algo do usuário

# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))
# altura = float(input("Digite sua altura: "))

# print(nome)
# print(type(idade))
# print(type(altura))


# Operadores aritméticos

# soma = 10 + 10
# multiplicacao = 10 * 10
# divisao = 10 / 10
# potencia = 2 ** 10

# print("soma", soma)
# print("multiplicacao", multiplicacao)
# print("divisao", divisao)
# print("potencia", potencia)


# Condicionais
# idade = int(input("Digite sua idade: "))

# if idade >= 18:
#     print("Você pode beber")
# else:
#     print("Você não pode beber")



# IF ELSE ELIF São estruturas de condição que permitem avaliar uma expressão e, de acordo com seu resultado, executar uma determinada ação.
# salario = float(input("Digite seu salário: "))

# if salario <= 3000:
#   print("Dev Junior")
# elif salario > 3000 and salario <= 6000:
#   print("Dev Pleno")
# elif salario > 6000 and salario <= 10000:
#   print("Dev Senior")
# else:
#   print("Project Manager")    


# Listas São coleções de elementos que podem ser de diferentes tipos, como inteiros, strings, floats, etc.

# lista_numeros = [1, 2, 3]

# lista_numeros[0] = 10

# print(lista_numeros[0])
# print(lista_numeros[1])
# print(lista_numeros[2])

# lista_vazia = []

# append serve para adicionar um elemento na lista
# lista_vazia.append("Hello")
# lista_vazia.append("World")

# print(lista_vazia)

# numeros = [10, 9, 8, 7, 6, 5]

# print("Total: ", len(numeros))
# print("Menor número: ", min(numeros))
# print("Maior número: ", max(numeros))


# For é uma estrutura de repetição que permite executar um bloco de código várias vezes.
notas = []

for x in range(10):
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print("Quantidade de notas", len(notas))  

for n in notas:
  codigo_aluno = n[0]
  nota = n[1]
  print("O RM: ", codigo_aluno, "Tirou a nota: ", nota)