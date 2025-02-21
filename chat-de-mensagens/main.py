# import os 

# mensagens = []

# nome = input("Nome: ")

# while True:
#   # limpando o terminal
#   os.system('cls')

#   if len(mensagens) > 0:
#     for m in mensagens:
#       print(m['nome'], "-", m['texto'])

#   print("_________________________")

#   # obtendo o texto

#   texto = input("mensagem: ")
#   if texto == "fim":
#     break

#   # adicionando mensagens na lista

#   mensagens.append ({
#     "nome": nome,
#     "texto": texto
#   })


  # Funções sao blocos de código que podem ser chamados em qualquer parte do código
  # Funções são definidas com a palavra reservada def

# def minha_funcao(valor1, valor2):
#     return valor1 + valor2

# while True:
#   valor1 = int(input("valor1: "))
#   valor2 = int(input("valor2: "))

#   resposta = minha_funcao(valor1, valor2)

#   print(valor1, "+", valor2, "=", resposta)


fluxo_caixa = []

print("_________________")
print("@ Fluxo caixa")
print("_________________")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("\n# Digite outro numero para encerrar #\n")

def adicionar_transacao():
  nome = input("Nome: ")
  valor = float(input("Valor: "))
  fluxo_caixa.append({
    "nome": nome,
    "valor": valor
  })

while True:
  opcao = int(input("Opção: "))

  if opcao == 1:
    adicionar_transacao()
  elif opcao == 2:
    adicionar_transacao()
  else:
    break

  # nota fiscal

  total = 0
  for fc in fluxo_caixa:
    print("Nome:", fc['nome'], "Valor: R$", fc['valor'])
    total = total + fc['valor']

  print("Saldo atual: R$", total)      