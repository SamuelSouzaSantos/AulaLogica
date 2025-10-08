# =================================================================
# 1. Sequência de Números Naturais Crescente
# =================================================================
valor_final = int(input("Digite o valor final da sequência crescente: "))

contador = 0
sequencia = []

for numero in range(1, valor_final + 1):
    sequencia.append(numero)
    contador += 1

print("A sequência gerada é:", sequencia)
print(f"Quantidade de valores na sequência: {contador}")


# =================================================================
# 2. Sequência de Números Naturais Decrescente
# =================================================================
valor_inicial = int(input("Digite o valor inicial da sequência decrescente (até zero): "))

contador = 0
sequencia = []

for numero in range(valor_inicial, -1, -1):
    sequencia.append(numero)
    contador += 1

print("A sequência gerada é:", sequencia)
print(f"Quantidade de valores na sequência: {contador}")


# =================================================================
# 3. Soma de Todos os Números no Intervalo de 1 a 500
# =================================================================
soma_total = 0

for numero in range(1, 501):
    soma_total += numero

print(f"A soma de todos os números inteiros de 1 a 500 é: {soma_total}")


# =================================================================
# 4. Soma de Ímpares Múltiplos de Três no Intervalo de 1 a 500
# =================================================================
soma_impar_multiplo_tres = 0

for numero in range(1, 501):
    if (numero % 2 != 0) and (numero % 3 == 0):
        soma_impar_multiplo_tres += numero

print(f"A soma dos números que são ÍMPARES E MÚLTIPLOS de 3 no intervalo de")