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
# notas = []

# for x in range(10):
#     codigo_aluno = input("RM: ")
#     nota = float(input("Nota: "))
#     resultado = [codigo_aluno, nota]
#     notas.append(resultado)

# print("Quantidade de notas", len(notas))  

# for n in notas:
#   codigo_aluno = n[0]
#   nota = n[1]
#   print("O RM: ", codigo_aluno, "Tirou a nota: ", nota)



# While é uma estrutura de repetição que permite executar um bloco de código várias vezes.
# notas = []
# contador = 1

# while contador <= 5:
#   codigo_aluno = input("RM: ")  
#   nota = float(input("Nota: "))
#   resultado = [codigo_aluno, nota]
#   notas.append(resultado)

#   contador = contador + 1

# print("Quantidade de notas", len(notas))

# Dicionários São estruturas que armazenam chave e valor.

# pessoa = {
#   "nome": "Matheus",
#   "idade": 24,
#   "altura": 1.80
# }

# print (pessoa["nome"])
# print (pessoa["idade"])
# print (pessoa["altura"])



# PLAYER INFO

player = {
  "nome": "Woozie",
  "rank": "Global",
  "arma": "AK-47",
  "hp": 100,
  "municao": 30
}

print(player["nome"])
print(player["rank"])
print(player["arma"])
print(player["hp"])
print(player["municao"])

# Lista de inimigos

npcs = [
  {"nome": "Malenia", "dano": 48, "hp": 1000, "exp": 100},
  {"nome": "Radahn", "dano": 68, "hp": 2000, "exp": 250},
  {"nome": "Mesmer", "dano": 46, "hp": 1200, "exp": 90},
  {"nome": "Radagon", "dano": 52, "hp": 1800, "exp": 180},
]

print(npcs[0]["nome"]), print(npcs[0]["dano"]), print(npcs[0]["hp"]), print(npcs[0]["exp"])
print(npcs[1]["nome"]), print(npcs[1]["dano"]), print(npcs[1]["hp"]), print(npcs[1]["exp"])
print(npcs[2]["nome"]), print(npcs[2]["dano"]), print(npcs[2]["hp"]), print(npcs[2]["exp"])
print(npcs[3]["nome"]), print(npcs[3]["dano"]), print(npcs[3]["hp"]), print(npcs[3]["exp"])

