from claseNodo import Nodo

class PilaEncadenada:
    __tope:Nodo
    __cant:int

    def __init__(self):
        self.__tope=None
        self.__cant=0

    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, dato):
        unNodo = Nodo(dato)
        unNodo.setSiguiente(self.__tope)
        self.__tope=unNodo
        self.__cant+=1


    def suprimir(self):
        if(self.vacia()):
            print("Lista vacia")
        else:
            aux=self.__tope.getDato()
            self.__tope=self.__tope.getSiguiente()
            self.__cant-=1
            return aux
        
    def recorrer(self):
        aux=self.__tope
        while aux!=None:
            print(aux.getDato())
            aux=aux.getSiguiente()


# if __name__ == "__main__":
#     pila = PilaEncadenada()
#     pila.insertar(5)
#     pila.insertar(8)
#     pila.insertar(9)
#     pila.insertar(15)
#     pila.recorrer()

        
         
        











  
		
            
    




        
	
			

