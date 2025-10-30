def converte_em_numeros(horas,minutos):
    vl_minutos = horas * 60 + minutos
    return vl_minutos

#Inicio do programa principal
if __name__ == '__main__':
    while True:

        h = int(input("Horas: "))
        if h == -1:
         break
        m = int(input("Minutos: "))
        retorno = converte_em_numeros(h,m)
        print("\n Horário em minutos:", retorno,"\n Horas:", h,"\n Minutos:", m)