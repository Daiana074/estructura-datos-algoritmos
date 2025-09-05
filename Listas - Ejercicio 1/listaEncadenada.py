from claseNodo import Nodo

class ListaEncadenada:
    __pri:Nodo   # Referencia al primer nodo de la lista
    __cont:int   # Cantidad de elementos en la lista

    def __init__(self):
        self.__pri=None     # Al inicio no hay nodos, la lista está vacía
        self.__cont=0       # Cantidad de elementos en 0

    def vacia(self):
        # Devuelve True si la lista no tiene elementos
        return self.__cont==0

    def primer_elemento(self):
        # Devuelve el dato almacenado en el primer nodo
        return self.__pri.getDato()

    def ultimo_elemento(self):
        # Recorre hasta el último nodo y devuelve su dato
        aux=self.__pri
        retorna=None
        while aux is not None:       # Avanza hasta que no haya más nodos
            retorna=aux.getDato()
            aux=aux.getSiguiente()
        return retorna

    def anterior(self,pos):
        # Devuelve el dato del nodo anterior a la posición indicada
        elemento=None
        if pos>0 and pos<=self.__cont-1:
            i=0
            aux=self.__pri
            # Avanza hasta el nodo anterior a "pos"
            while i < pos-1:
                aux=aux.getSiguiente()
                i+=1
            elemento=aux.getDato()
        else:
            print("El indice ingresado no es valido")
        return elemento

    def siguiente(self,pos):
        # Devuelve la posición siguiente si existe
        p=None
        if pos>=0 and pos<self.__cont-1:
            p=pos+1
        else:
            print("El indice ingresado no es valido")
        return p

    def insertar(self,item,pos):
        # Inserta un nuevo nodo con "item" en la posición "pos"
        nuevoNodo=Nodo(item)
        if pos>=0 and pos<=self.__cont:
            if pos==0:   # Caso especial: insertar al inicio
                nuevoNodo.setSiguiente(self.__pri)
                self.__pri=nuevoNodo
                self.__cont+=1
            else:
                aux=self.__pri
                indice=0
                # Recorre hasta la posición donde se insertará
                while pos != indice:
                    anterior=aux
                    aux=aux.getSiguiente()
                    indice+=1
                anterior.setSiguiente(nuevoNodo)
                nuevoNodo.setSiguiente(aux)
                self.__cont+=1
        else:
            print("El indice ingresado no es valido")

    def suprimir(self,pos):
        # Elimina el nodo en la posición indicada y devuelve su dato
        elemento=None
        if self.vacia():
            print("Pila Vacia, no se pueden eliminar elementos")
        else:
            if pos>=0 and pos<self.__cont:
                aux=self.__pri
                if pos==0:   # Caso especial: eliminar el primer nodo
                    self.__pri=aux.getSiguiente()
                else:
                    ant=aux
                    aux=aux.getSiguiente()
                    i=1
                    # Recorre hasta el nodo que se quiere eliminar
                    while i<pos:
                        ant = aux
                        aux=aux.getSiguiente()
                        i+=1
                    # "saltea" el nodo a eliminar
                    ant.setSiguiente(aux.getSiguiente())
                self.__cont-=1
                elemento=aux.getDato()
        return elemento

    def buscar(self,item):
        # Busca un item en la lista y devuelve su posición
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
        # Devuelve el dato en la posición indicada
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
        # Recorre la lista y muestra todos los datos
        aux=self.__pri
        while aux is not None:
            print(aux.getDato())
            aux=aux.getSiguiente()

if __name__=="__main__":
    l=ListaEncadenada()
    l.insertar(-5,0)
    l.insertar(-7,1)
    l.insertar(-2,2)
    l.recorrer()
    print("Desplazamiento")
    l.insertar(-9,1)
    l.recorrer()
    print("Desplazamiento")
    l.insertar(-18,4)
    l.recorrer()
    print("Desplazamiento")
    l.insertar(-84,0)
    l.recorrer()
    print("El primer elemento es: ",l.primer_elemento())
    print("El ultimo elemento es: ",l.ultimo_elemento())
    print("Se elimina el ",l.suprimir(2))
    l.recorrer()
    print("Se elimina el ",l.suprimir(0))
    l.recorrer()
    print("El primer elemento es: ",l.primer_elemento())
    print("Se elimina el ",l.suprimir(1))
    l.recorrer()
    print("El elemento -5 esta en la posicion: ",l.buscar(-5))
    print("El elemento -18 esta en la posicion: ",l.buscar(-18))
    print("El elemento -2 esta en la posicion: ",l.buscar(-2))
    print("El elemento -50 esta en la posicion: ",l.buscar(-50))
    print("En la posicion 1 hay un ", l.recuperar(1))
    print("El elemento siguiente a la posicion 1 es: ",l.siguiente(1))
    print("El elemento anterior a la posicion 1 es: ",l.anterior(1))
    print("El elemento anterior a la posicion 2 es: ",l.anterior(2))
    print("El elemento siguiente a la posicion 2 es: ",l.anterior(0))
