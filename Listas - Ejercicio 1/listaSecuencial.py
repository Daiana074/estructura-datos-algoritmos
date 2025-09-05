
import numpy as np  # Importamos NumPy para manejar un arreglo de tamaño fijo y acceso O(1).

class ListaSecuencial:
    __ult:int              # Cantidad de elementos cargados (también indica la próxima posición libre).
    __dimension:int        # Capacidad máxima del arreglo.
    __arregloDatos:np.ndarray  # Arreglo físico donde se almacenan los datos.

    def __init__(self,dimension=5):
        self.__ult=0                          # Inicialmente la lista está vacía (0 elementos).
        self.__dimension=dimension            # Guardamos la capacidad máxima.
        self.__arregloDatos=np.empty(dimension,dtype=int)  
        # Creamos el arreglo con 'dimension' lugares. dtype=int => solo enteros.
        # Si quisieras almacenar distintos tipos (strings, objetos, etc.), usar dtype=object.

    def vacia(self):
        return self.__ult==0                  # La lista está vacía si no hay elementos cargados.

    def llena(self):
    # Devuelve True si la lista alcanzó la dimensión máxima
        return self.__ult == self.__dimension

    def siguiente(self,pos):
        p1=None
        # 'siguiente' de 'pos' existe si pos está en [0, __ult-2]. 
        # Ej: si __ult=5, posiciones válidas: 0..4; el "siguiente" de 4 no existe.
        if pos>=0 and pos<self.__ult-1:
            p1=pos+1                          # Devolvemos la posición siguiente.
        else:
            print("El indice ingresado no es valido")  # Mensaje si no hay siguiente o el índice es inválido.
        return p1

    def anterior(self,pos):
        p1=None
        # 'anterior' de 'pos' existe si pos está en [1, __ult-1].
        if pos>0 and pos<=self.__ult-1:
            p1=pos-1                          # Devolvemos la posición anterior.
        else:
            print("El indice ingresado no es valido")  # Mensaje si no hay anterior o el índice es inválido.
        return p1

    def primer_elemento(self):
        return self.__arregloDatos[0]         # Devuelve el primer elemento (PRECOND: la lista no debe estar vacía).

    def ultimo_elemento(self):
        return self.__arregloDatos[self.__ult-1]  # Devuelve el último cargado (PRECOND: no vacía).

    def insertar(self,item,pos):
        # Insertar 'item' en la posición 'pos' (0 <= pos <= __ult), desplazando a la derecha.
        if self.__ult < self.__dimension:     # Verificamos que haya espacio en el arreglo.
            if pos>=0 and pos<=self.__ult:    # La posición válida es entre 0 y __ult inclusive.
                i= self.__ult                 # i arranca en la última posición ocupada (próxima libre).
                while i>pos:                  # Desplazamos elementos a la derecha hasta abrir hueco en 'pos'.
                    self.__arregloDatos[i]=self.__arregloDatos[i-1]
                    i-=1
                self.__arregloDatos[i]=item   # Colocamos el nuevo elemento en 'pos'.
                self.__ult+=1                 # Aumentamos la cantidad de elementos cargados.
            else:
                print("El indice ingresado no es valido")  # Posición fuera de rango permitido.
        else:
            print(f"No es posible insertar el elemento {item}. Lista llena")  # No hay capacidad.

    def recorrer(self):
        # Recorremos e imprimimos los elementos cargados (de 0 a __ult-1).
        for i in range(self.__ult):
            print(self.__arregloDatos[i])

    def buscar(self,item):
        # Búsqueda secuencial: devuelve la posición del 'item' o None si no está.
        i=0
        posicion=None
        band=False
        # ⚠️ IMPORTANTE: la condición correcta es i < self.__ult (no <=) para evitar IndexError.
        # En el código original decía "i<=self.__ult", lo CORREGIMOS acá.
        while i<self.__ult and band is False:
            if self.__arregloDatos[i]==item:  # Comparamos el elemento actual con 'item'.
                posicion=i                    # Si coincide, guardamos la posición...
                band=True                     # ...y cortamos la búsqueda.
            else:
                i+=1                          # Si no coincide, seguimos con el siguiente índice.
        return posicion                       # Devuelve la posición encontrada o None.

    def recuperar(self,pos):
        # Devuelve el elemento almacenado en 'pos', si es válida.
        elemento= None
        if pos>=0 and pos<self.__ult:         # 'pos' debe estar dentro de los elementos cargados.
            elemento= self.__arregloDatos[pos]
        else:
            print("El indice ingresado no es valido")  # Índice inválido.
        return elemento

    def suprimir(self,pos):
        # Elimina el elemento en 'pos' y devuelve dicho elemento.
        elemento=None
        if pos>=0 and pos<self.__ult:         # 'pos' debe apuntar a un elemento cargado.
            elemento=self.__arregloDatos[pos] # Guardamos el elemento a devolver.
            # Desplazamos a la izquierda desde 'pos' hasta el penúltimo elemento cargado.
            for i in range(pos,self.__ult-1):
                self.__arregloDatos[i]= self.__arregloDatos[i+1]
            self.__ult-=1                     # Reducimos la cantidad de elementos.
            # Nota: no es necesario "borrar" el último valor viejo; queda basura pero fuera de __ult.
        else:
            print("El indice ingresado no es valido")  # Índice inválido para suprimir.
        return elemento


if __name__=="__main__":
    l=ListaSecuencial()
    l.insertar(-9,0)
    l.insertar(-3,1)
    l.recorrer()
    print("Desplazamiento")
    l.insertar(-2,1)
    l.recorrer()
    print("Desplazamiento")
    l.insertar(-7,3)
    l.recorrer()
    print("Lista llena?: ",l.llena())
    print("Desplazamiento")
    l.insertar(-15,0)
    l.recorrer()
    l.insertar(-99,2)
    print("Lista llena?: ",l.llena())
    print("El primero es: ",l.primer_elemento())
    print("El ultimo es: ",l.ultimo_elemento())
    print("El elemento -9 se encuentra en el indice: ",l.buscar(-9))
    print("El elemento siguiente a la posicion 2 es: ",l.siguiente(2))
    print("El elemento anterior a la posicion 2 es: ",l.anterior(2))

    print("Sumprimido en pos 2: ",l.suprimir(2))
    l.recorrer()
    print("Sumprimido en pos 0: ",l.suprimir(0))
    l.recorrer()
    print("Sumprimido en pos 2: ",l.suprimir(2))
    l.recorrer()
    print("insercion")
    l.insertar(-12,2)
    l.recorrer()
