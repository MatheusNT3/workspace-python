# Operadores aritméticos

# Soma = +
soma = 5 + 2
print(soma)

# Subtração = -
subtracao = 5 - 2
print(subtracao)

# Multiplicação = *
multiplicacao = 5 * 2
print(multiplicacao)

# Divisão = /
divisao = 5 / 2
print(divisao)

# Divisão inteira = //
divisao_inteira = 5 // 2
print(divisao_inteira)

# Resto da divisão = %
resto_divisao = 5 % 2
print(resto_divisao)

# Potência = **
potencia = 5 ** 2
print(potencia)

# Raiz quadrada = **(1/2)
raiz_quadrada = 25 ** (1/2)
print(raiz_quadrada)

# Raiz cúbica = **(1/3)
raiz_cubica = 27 ** (1/3)
print(raiz_cubica)



# ORDEN DE PRECEDÊNCIA

# 1. ()
# 2. **
# 3. *, /, //, %
# 4. +, -
# 5. =


n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print(f'A soma é {s}, o produto é {m} e a divisão é {d:.2f}')

