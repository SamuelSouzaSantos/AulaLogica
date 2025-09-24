idade = int(input("Digite a idade do animal: "))
if idade < 4:
    print("Animal Jovem")
elif idade > 4 and idade <10:
    print("Animal Adulto")
else:
    print("Animal Idoso")

print(f"Idade do Animal: {idade}")

impar = 0
soma = 0
ct = 0
while True:
    numero = int(input("Digite um número: "))
    if numero == -1:
        break
    if numero % 2 == 1:
        impar = impar + 1
    ct = ct + 1
    soma = numero + soma
media = soma / ct
print(f"A quantidade de valores é igual a: {ct}")
print(f"A soma dos {ct} números é igual a: {soma}")
print(f"A média das soma {soma} é igual a: {media:.4}")
print(f"Dos {ct} números, {impar} números são ímpares!")