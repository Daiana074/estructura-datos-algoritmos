import numpy as np

class ListaSecuencialContenido:
    __ult:int
    __arregloDatos:np.ndarray

    def __init__(self):
        # __ult guarda la cantidad de elementos actualmente en la lista
        self.__ult = 0
        # arreglo físico donde guardamos los elementos; tamaño fijo (5) y tipo int
        self.__arregloDatos = np.empty(5, dtype=int)

    def vacia(self):
        # Devuelve True si no hay elementos
        return self.__ult == 0

    def llena(self):
        # Devuelve True si ya alcanzamos la capacidad del arreglo
        return self.__ult == len(self.__arregloDatos)

    def siguiente(self, item):
        elemento = None
        # Solo tiene sentido buscar siguiente si la lista no está vacía
        if not self.vacia():
            pos = 0
            # Buscamos la posición donde esté el item (o llegamos al fin)
            while pos < self.__ult and item != self.__arregloDatos[pos]:
                pos += 1

            # Si pos != __ult entonces lo encontramos; si pos == __ult no está
            if pos != self.__ult:
                # Si está en la última posición no tiene siguiente
                if pos == self.__ult - 1:
                    print("El elemento ingresado no cuenta con un siguiente en la lista; es el ultimo")
                else:
                    # Devolvemos el dato en la posición siguiente
                    elemento = self.__arregloDatos[pos + 1]
            else:
                # No lo encontramos en la lista
                print("El elemento ingresado no se encuentra en la lista")
        else:
            # Lista vacía: no puede existir el elemento
            print("Pila Vacia. No existe el elemento ingresado")
        return elemento

    def anterior(self, item):
        elemento = None
        # Solo buscamos anterior si la lista no está vacía
        if not self.vacia():
            pos = 0
            # Buscamos la posición del item
            while pos < self.__ult and item != self.__arregloDatos[pos]:
                pos += 1

            if pos != self.__ult:
                # Si está en la primera posición no tiene anterior
                if pos == 0:
                    print("El elemento ingresado no cuenta con un anterior en la lista; es el primero")
                else:
                    # Devolvemos el dato en la posición anterior
                    elemento = self.__arregloDatos[pos - 1]
            else:
                # Item no encontrado
                print("El elemento ingresado no se encuentra en la lista")
        else:
            # Lista vacía
            print("Pila Vacia. No existe el elemento ingresado")
        return elemento

    def primer_elemento(self):
        # Devuelve el primer elemento (PRECONDICIÓN: la lista no debe estar vacía)
        return self.__arregloDatos[0]

    def ultimo_elemento(self):
        # Devuelve el último elemento cargado (PRECONDICIÓN: la lista no debe estar vacía)
        return self.__arregloDatos[self.__ult - 1]

    def localizar_posicion(self, item):
        # Devuelve la posición donde insertar el item para mantener orden creciente.
        # CORRECCIÓN: hay que asegurarse de no leer fuera de los elementos válidos.
        # Por eso iteramos solo hasta __ult (no hasta len(__arregloDatos)).
        i = 0
        # Mientras no lleguemos al final de los elementos y el elemento actual sea menor que item
        while i < self.__ult and self.__arregloDatos[i] < item:
            i += 1
        # i será la posición donde debe quedar 'item' (puede ser al final si todos son menores)
        return i

    def insertar(self, item):
        # Inserta el item manteniendo la lista ordenada (si hay espacio)
        if self.__ult < len(self.__arregloDatos):
            # Calculamos la posición ordenada donde insertar
            pos = self.localizar_posicion(item)
            # Desplazamos a la derecha desde la última posición hasta abrir espacio en pos
            i = self.__ult
            while i > pos:
                self.__arregloDatos[i] = self.__arregloDatos[i - 1]
                i -= 1
            # Colocamos el nuevo elemento en la posición abierta
            self.__arregloDatos[i] = item
            # Aumentamos el contador de elementos
            self.__ult += 1
        else:
            # No hay lugar en el arreglo
            print(f"No es posible insertar el elemento {item}. Lista llena")

    def recorrer(self):
        # Imprime todos los elementos desde 0 hasta __ult-1
        for i in range(self.__ult):
            print(self.__arregloDatos[i])

    def buscar(self, item):
        # Búsqueda secuencial: devuelve la posición o None si no lo encuentra
        i = 0
        posicion = None
        band = False
        # Recorremos solo los elementos cargados (0..__ult-1)
        while i < self.__ult and band is False:
            if self.__arregloDatos[i] == item:
                posicion = i
                band = True
            else:
                i += 1
        # Si no lo encontró devuelve None (el print está comentado en el original)
        return posicion

    def recuperar(self, pos):
        # Recupera el elemento en la posición pos si es válida
        elemento = None
        if pos >= 0 and pos < self.__ult:
            elemento = self.__arregloDatos[pos]
        else:
            print("En indice ingresado no es valido")
        return elemento

    def suprimir(self, item):
        # Suprime el elemento por contenido (no por posición). Devuelve la posición si lo eliminó.
        pos = None
        if not self.vacia():
            pos = self.buscar(item)  # Buscamos dónde está
            if pos is not None:
                # Desplazamos a la izquierda desde pos hasta __ult-2
                for i in range(pos, self.__ult - 1, 1):
                    self.__arregloDatos[i] = self.__arregloDatos[i + 1]
                # Reducimos la cantidad de elementos (el "último" queda con basura pero fuera de rango)
                self.__ult -= 1
            else:
                print(f"El elemento {item} no se encuentra en la lista. Por ende, no se puede suprimir")
        else:
            print(f"No se puede suprimir el elemento {item}. La lista esta vacia")
        return pos


if __name__=="__main__":
    l=ListaSecuencialContenido()
    l.insertar(-5)
    l.insertar(-3)
    l.insertar(-6)
    l.insertar(-10)
    l.insertar(-1)
    l.insertar(-87)
    l.recorrer()
    print("Se suprime el elemento -10 del indice: ",l.suprimir(-10))
    l.recorrer()
    print("Se suprime el elemento -1 del indice: ",l.suprimir(-1))
    l.recorrer()
    print("Se suprime el elemento -99 del indice: ",l.suprimir(-99))
    l.recorrer()
    print("El anterior al elemento -5 es: ",l.anterior(-5))
    print("El siguiente al elemento -6 es: ",l.siguiente(-6))
