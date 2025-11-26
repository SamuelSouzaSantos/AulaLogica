from mailbox import Maildir


soma_idades = 0
ct = 0
maisNovo = 9999999
ct_menor_idade = 0
for i in range(1,51):
    idade = int(input("Idade do aluno: "))
    soma_idades += idade
    ct +=1
    if idade < 18:
        ct_menor_idade += 1
    if idade < maisNovo:
        maisNovo = idade
    
media = soma_idades / ct
print("\n--- Relatório Estatístico ---")
print("Media", media)
print(f"mais novo {maisNovo}")
print(f"idademais novo {ct_menor_idade}")