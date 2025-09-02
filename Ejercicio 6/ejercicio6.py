
#from colaEncadenada import ColaEncadenada
from colaSecuencial import ColaSecuencial
class EscalerasNoRecursivo:
    
    def __init__(self, n):
        self.__n = n                  # Cantidad total de peldaños
        self.listar_formas()        # Llamamos al método principal para listar todas las formas

    def listar_formas(self):
        cola = ColaSecuencial()      # Creamos una pila vacía
        cola.insertar(("", self.__n))  # Insertamos la tupla: (resParcial, escalones_restantes)

        # Mientras la pila no esté vacía
        while not cola.vacia():
            resParcial, escalones = cola.suprimir()  # Sacamos un elemento del tope

            if escalones == 0:
                # Si no quedan escalones, mostramos la secuencia completa
                print(resParcial.strip())
            else:
                # Si quedan escalones, agregamos nuevas opciones a la pila
                # Primero agregamos "2" si se puede subir de dos en dos
                if escalones >= 2:
                    cola.insertar((resParcial + " 2", escalones - 2))
                # Luego agregamos "1" si se puede subir de uno en uno
                if escalones >= 1:
                    cola.insertar((resParcial + " 1", escalones - 1))

# Ejemplo de uso:
escalera = EscalerasNoRecursivo(5)
