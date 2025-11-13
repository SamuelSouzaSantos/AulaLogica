# CRUD acrônimo de Create, Read, Update and Delete (inclui, consulta, atualiza e apaga os dados)
l_nomes = []
def menu():
    print('[c] - Create')
    print('[r] - Read')
    print('[u] - Update')
    print('[d] - Delete')
    print('[e] - Exit')
    opcao = input("Opção: ")
    return opcao
def create():
    ct=0
    while True:
        nome = str(input("Digite o nome: "))
        if nome != 0:
            ct+=1
        if nome == '0':
            break
        l_nomes.append(nome)
    print(f"Quantidades de nomes adicionados:{ct}:")
def read():
    print(f'O nome na lista é:{l_nomes}')
def update():
    att = str(input('digite um novo nome:'))
    nv_nm = int(input('digite a posição do nome'))
    l_nomes[nv_nm] = att
def delete():
    escolha = int(input("ESCOLHA:\n [1] para apagar pelo nome:\n [2] para apagar pelo indíce:\n"))
    if escolha == 1:
        dell = str(input('digite o nome que deseja remover:'))
        l_nomes.remove(dell)
    else:
        dell1 = int(input('digite a possição do nome a ser deletado:'))
        l_nomes.pop(dell1)
if __name__ == '__main__':
    while True:
        op = menu()
        if op == 'c':
            create()
        elif op == 'r':
            read()
        elif op == 'u':
            update()
        elif op == 'd':
            delete()
        else:
            break


