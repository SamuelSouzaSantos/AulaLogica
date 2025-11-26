def calculadora(coloqueOParametro):
    idade = ( 2025 - coloqueOParametro )
    return idade
if __name__ == '__main__':
    ano = int(input("Ano de nascimento"))
    print(f"A idade da pessoa é igual a {calculadora(ano)}")