# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
# s = n1 + n2
# print(f"A soma de {n1} e {n2} é {s}.")

# Solicita uma entrada do usuário
teste = input("Digite algo: ")

# Exibe o tipo primitivo da entrada
print(f"O tipo primitivo desse valor é {type(teste)}")

# Exibe outras informações sobre a entrada
print(f"Só tem espaços? {teste.isspace()}")
print(f"É um número? {teste.isnumeric()}")
print(f"É alfabético? {teste.isalpha()}")
print(f"É alfanumérico? {teste.isalnum()}")
print(f"Está em maiúsculas? {teste.isupper()}")
print(f"Está em minúsculas? {teste.islower()}")
print(f"Está capitalizada? {teste.istitle()}")