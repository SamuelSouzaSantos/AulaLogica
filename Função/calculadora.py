def somador(valor1,valor2, valor3):
    soma = valor1 + valor2 + valor3
    return soma

if __name__ == '__main__':
    valor1 = int(input('Digite o valor 1: '))
    valor2 = int(input('Digite o valor 2: '))
    valor3 = int(input('Digite o valor 3: '))
    print(f"A soma dos valores {valor1}, {valor2} e {valor3} é igual a: {somador(valor1,valor2,valor3)}")