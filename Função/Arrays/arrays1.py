#Manutenção de uma lista ou CRUD:
#CRUD (Create, REad, Updtate, Delete) - criar, ler, atualizar, deletar
lista = [1,2,3,4,5]
print(lista)

for item in lista:
    print(item)

lista = [10,20,30,40]

if 300 in lista:
    print("Valor na lista")
else: print("Não está na lista")

lista1 = [3,'abacate', 9.7, [5,6,3], "Python"], (3,'j')

novoValor = int(input("Novo valor:"))
indice = int(input("Qual a posição do (índice): "))
#Usando notacao de vetor
lista1[indice] = novoValor