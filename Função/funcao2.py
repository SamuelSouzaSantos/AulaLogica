def minimo_dois(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

def maximo_dois(num1, num2):
    if num1 > num2:
        maximo = num1
    else:
        maximo = num2
    return maximo

def sem_variavel(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

print('-------------------MÁXIMO VALOR ---------------')

if __name__ == '__main__':
    num1 = int(input("Digite o primeiro número:"))
    num2 = int(input("Digite o segundo número:"))
    print(f"O maior valor é igual a: {maximo_dois(num1,num2)}")

    print('-------------------MÍNIMO VALOR ---------------')
    num1 = int(input("Digite o primeiro número:"))
    num2 = int(input("Digite o segundo número:"))
    print(f"O menor valor é igual a:{minimo_dois(num1,num2)}")


print('-------------------SEM VARIÁVEL---------------')
if __name__ == "__main__":
    num1 = int(input("Digite o primeiro número:"))
    num2 = int(input("Digite o segundo número:"))
    print(f"O maior valor é igual a: {sem_variavel(num1,num2)}")
