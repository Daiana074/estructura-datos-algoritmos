from pilaEncadenada import PilaEncadenada

if __name__=="__main__":
    #instanciamos
    p=PilaEncadenada()
    try:
        #ingresamo el decimal
        decimal=int(input("Ingresa el numero decimal: "))
        #guardamos el decimal en un auxiliar
        aux=decimal
        #mientras aux sea mayo o igual que 1
        while aux>=1:
            #resto
            modulo=aux%2
            aux=aux//2
            p.insertar(modulo)
    except ValueError:
        print("Error. Se esperaba un entero")
        
    print("En binario es: ",end=" ")
    while p.vacia() is False:
        print(p.suprimir(),end="")