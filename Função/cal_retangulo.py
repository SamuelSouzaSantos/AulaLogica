def area_retangulo (base,altura):
    area = base * altura
    return area

if __name__ == '__main__':
    base = int(input("Entre com o base: "))
    altura = int(input("Entre com o altura: "))
    print(f"A aréa desse retângulo é igual a: {area_retangulo(base,altura)}")
    print("A aréa desse retângulo é igual a: ", area_retangulo(base,altura))