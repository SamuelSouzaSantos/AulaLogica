vazia = []
maior10 = []
print("Digite [0] para sair")
while True:
    numero = int(input("Digite um valor "))
    if numero > 10:
        maior10 = numero
    if numero == 0:
        break
    vazia.append(numero)
print("Valores da lista na horizontal", vazia)

for i in vazia:
    print(i)

print("Quantidade de elementos da lista: ", len(vazia))

print("Soma dos valores da lista", sum(vazia))

print("Maior valor da lista:", max(vazia))

print("Maior valor da lista:", min(vazia))

pesquisa = int(input("Digite o valor a ser procurado: "))
if pesquisa in vazia:

    print(f"O valor {pesquisa} está na lista: {vazia}, se encontra na posição",vazia.index(pesquisa))

else: print("O valor não se encontra na lista!")

print(f"Antes do sort():\n{vazia}")
vazia.sort()
print(f"Depois do sort():\n{vazia}")

vazia.insert(1,33)
print(vazia)

vazia.sort()
vazia.reverse()
print(vazia)

media = (sum(vazia)/len(vazia))
print(f"A média aritmética dos {len(vazia)} valores da lista é igual a {media:.3}")

print(f"Dos {len(vazia)}, {maior10} são maiores que 10")