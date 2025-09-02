#from claseNodo import Nodo
from pilaEncadenada import PilaEncadenada

class EscalerasNoRecursivo:
    
    def __init__(self, n):
        self.__n = n                  # Cantidad total de peldaños
        self.listar_formas()        # Llamamos al método principal para listar todas las formas

    def listar_formas(self):
        pila = PilaEncadenada()      # Creamos una pila vacía
        pila.insertar(("", self.__n))  # Insertamos la tupla: (resParcial, escalones_restantes)

        # Mientras la pila no esté vacía
        while not pila.vacia():
            resParcial, escalones = pila.suprimir()  # Sacamos un elemento del tope

            if escalones == 0:
                # Si no quedan escalones, mostramos la secuencia completa
                print(resParcial.strip())
            else:
                # Si quedan escalones, agregamos nuevas opciones a la pila
                # Primero agregamos "2" si se puede subir de dos en dos
                if escalones >= 2:
                    pila.insertar((resParcial + " 2", escalones - 2))
                # Luego agregamos "1" si se puede subir de uno en uno
                if escalones >= 1:
                    pila.insertar((resParcial + " 1", escalones - 1))

# Ejemplo de uso:
escalera = EscalerasNoRecursivo(5)
