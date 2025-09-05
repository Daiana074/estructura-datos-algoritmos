from claseNodo import Nodo   # Importamos la clase Nodo para armar la lista encadenada

class ListaEncadenada:
    __pri:Nodo     # Puntero al primer nodo de la lista
    __cont:int     # Contador de elementos en la lista

    def __init__(self):
        self.__pri=None    # Al inicio la lista está vacía → no hay primer nodo
        self.__cont=0      # Contador en cero porque no hay elementos

    def vacia(self):
        # Devuelve True si la lista no tiene elementos
        return self.__cont==0

    def primer_elemento(self):
        # Devuelve el dato del primer nodo
        return self.__pri.getDato()

    def ultimo_elemento(self):
        # Recorre la lista hasta el final para devolver el último elemento
        aux=self.__pri
        retorna=None
        while aux is not None:
            retorna=aux.getDato()
            aux=aux.getSiguiente()
        return retorna

    def anterior(self,item):
        # Devuelve el elemento anterior al "item" recibido
        elemento=None
        if not self.vacia():    # Si la lista no está vacía
            aux1=self.__pri
            pos=0
            # Busco la posición del nodo que contiene "item"
            while aux1 is not None and aux1.getDato()!=item:
                pos+=1
                aux1=aux1.getSiguiente()
            if aux1 is not None:   # Si encontré el item
                if pos==0:
                    # Si está en la primera posición, no tiene anterior
                    print("El elemento ingresado no cuenta con un anterior. Es el primero")
                else:
                    # Si no es el primero, me muevo hasta la posición previa
                    aux2=self.__pri
                    for i in range(pos-1):
                        aux2=aux2.getSiguiente()
                    elemento=aux2.getDato()
            else:
                # Si no lo encontré en toda la lista
                print(f"El elemento {item} no se encuentra en la lista")
        else:
            print("Pila Vacia. No existe el elemento",item)
        return elemento

    def siguiente(self,item):
        # Devuelve el elemento siguiente al "item" recibido
        elemento=None
        if not self.vacia():
            aux1=self.__pri
            pos=0
            # Busco la posición del nodo que contiene "item"
            while aux1 is not None and aux1.getDato()!=item:
                pos+=1
                aux1=aux1.getSiguiente()
            if aux1 is not None:
                if pos==self.__cont-1:
                    # Si está en la última posición, no tiene siguiente
                    print("El elemento ingresado no cuenta con un siguiente. Es el ultimo")
                else:
                    # Me muevo hasta el siguiente nodo y devuelvo el dato
                    aux2=self.__pri
                    for i in range(pos+1):
                        aux2=aux2.getSiguiente()
                    elemento=aux2.getDato()
            else:
                print(f"El elemento {item} no se encuentra en la lista")
        else:
            print("Pila Vacia. No existe el elemento",item)
        return elemento

    def localizar_posicion(self,item):
        # Busca en qué posición debería insertarse el item para mantener el orden
        i=0
        aux=self.__pri
        # Avanza mientras los elementos sean menores al item
        while aux is not None and aux.getDato()<item:
            i+=1
            aux=aux.getSiguiente()
        return i   # Devuelve la posición calculada

    def insertar(self,item):
        # Inserta un nuevo nodo en la posición correcta para mantener la lista ordenada
        nuevoNodo=Nodo(item)
        pos=self.localizar_posicion(item)
        if pos==0:
            # Insertar al inicio
            nuevoNodo.setSiguiente(self.__pri)
            self.__pri=nuevoNodo
            self.__cont+=1
        else:
            # Insertar en medio o al final
            aux=self.__pri
            indice=0
            while pos != indice:
                anterior=aux
                aux=aux.getSiguiente()
                indice+=1
            anterior.setSiguiente(nuevoNodo)
            nuevoNodo.setSiguiente(aux)
            self.__cont+=1

    def suprimir(self,item):
        # Elimina un nodo que contenga el "item"
        pos=None
        if self.vacia():
            print("Pila Vacia, no se pueden eliminar elementos")
        else:
            pos=self.buscar(item)   # Busco en qué posición está el item
            if pos is not None:
                aux=self.__pri
                if pos==0:   # Si es el primero
                    self.__pri=aux.getSiguiente()
                else:
                    # Si está en el medio/final, avanzo hasta llegar a él
                    ant=aux
                    aux=aux.getSiguiente()
                    i=1
                    while i<pos:
                        ant = aux
                        aux=aux.getSiguiente()
                        i+=1
                    # El nodo "ant" ahora salta el nodo "aux"
                    ant.setSiguiente(aux.getSiguiente())
                self.__cont-=1
            else:
                print(f"El elemento {item} no está en la lista. Por ende no puede ser suprimido")
        return pos

    def buscar(self,item):
        # Busca un item en la lista y devuelve su posición si lo encuentra
        aux=self.__pri
        band=False
        pos=None
        i=0
        while aux is not None and band is False:
            if aux.getDato()==item:
                pos=i
                band=True
            else:
                aux=aux.getSiguiente()
                i+=1
        return pos

    def recuperar(self,pos):
        # Devuelve el elemento en la posición indicada
        aux=self.__pri
        i=0
        if pos>=0 and pos<self.__cont:
            while i!=pos:
                aux=aux.getSiguiente()
                i+=1
            elemento= aux.getDato()
        else:
            elemento=None
            print("El indice ingresado no es valido")
        return elemento
                
    def recorrer(self):
        # Recorre la lista imprimiendo todos sus elementos
        aux=self.__pri
        while aux is not None:
            print(aux.getDato())
            aux=aux.getSiguiente()


if __name__=="__main__":
    l=ListaEncadenada()
    l.insertar(-5)
    l.insertar(-7)
    l.insertar(-2)
    l.insertar(6)
    l.recorrer()
    print("Se suprimio el elemento 6 de la posicion: ",l.suprimir(6))
    l.recorrer()
    print("ant: ",l.anterior(-5))
    print("sig: ",l.siguiente(-5))