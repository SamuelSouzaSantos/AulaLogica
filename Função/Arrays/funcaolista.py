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
    print('Em desenvolvimento - create')
def read():
    print('Em desenvolvimento - read')
def update():
    print('Em desenvolvimento - update')
def delete():
    print('Em desenvolvimento - delete')
if __name__ == 'main':
    while True:
        op = menu()
        if op == 'c':
            create()
        if op == 'r':
            read()
        if op == 'u':
            update()
        if op == 'd':
            delete()
        else:
            break


