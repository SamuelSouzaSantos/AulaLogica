#A função é o principal e mais importante meio de organização e reutilização de código. Se precisar repetir o mesmo código é melhor escrever uma função reutilizável. 
#A função em python é definida com a palavra-chave def
#def nome_funcao(par1,par2,...,para):
    #Bloco de códig0 da função
   # return ValueError
#-obs.: pode ou não receber parametros; uma função pode ou não retornar um valor 

#-chamar (usar) a função criada, dento do main (programa)

#dois tipos de função (retorna e a que nao retorna)
def mostra_mensagem():
    print("Exemplo de mensagem fixa em def.")
if __name__ =="__main__":
    print("Mensagem antes de chamar a função") #No inicio do main
    mostra_mensagem()
    print("Mensagem depois de chamar a função")

#2.1 sinntaxe:

#def nome_funcao(par1,par2,...,para): #os parametros sao opcionais
    #Bloco de códig0 da função
#    return valor                     #RETURN    

#2.2
def calcula_dobro(p_valor):
    dobro = p_valor * 2
    return dobro

if __name__ =="__main__":
    valor=int(input("valor Inteiro:"))
    v_retornado = calcula_dobro(valor) #chama a função
    #A variavel v_reornado recebe o calor retornado pela função (def)
    #O valor retornado pelafunção é armazenado na variavel bv_retrnado
    print("Valor retornado pela função:", v_retornado)


# o return sempre vai ser usado para retornar um valor do processamento da função para pegar o valor da variavel na funçaõ e colocar na variavel outra local

def mostra_valor(valor):
    print("Parametro recebido:", valor)
if __name__ =="__main__":
    print("primeira forma de fazer (sem variáveis, passa o valor direto:)")
    mostra_valor(5)
    mostra_valor(23.8)

def retorna_soma(valor1,valor2):
    soma = valor1 + valor2
    return soma

def retorna_sub(valor1,valor2):
    sub = valor1 - valor2
    return sub

if __name__ =="__main__": 
    x1 = int(input("Digite o numero: "))
    x2 = int(input("Digite o numero: "))
    print("A soma dos dois valores é igual à:", retorna_soma(x1,x2))
    print("A subtração dos dois valores é igual à:", retorna_sub(x1,x2))

if __name__ =="__main__": 
    v1 = int(input("Primeiro valor:"))
    v2 = int(input("Segundo valor:"))
    opcao = int(input("[1] SOMAR\n[2] SUBTRAÇÃO\nOpção: "))
    if opcao== 1:
        print("\nSoma =", retorna_soma(v1,v2))
    else:
        print("\nSubtracao =", retorna_sub(v1,v2))
print("FINALIZADO")