from pilaEncadenada import PilaEncadenada  # Importa la clase de pila encadenada que creaste

class TorresdeHanoi:
    def __init__(self, n):
        self.__n = n                        # Guarda la cantidad de discos (privado)
        self.__torre1 = PilaEncadenada()    # Inicializa torre 1 (donde empiezan los discos)
        self.__torre2 = PilaEncadenada()    # Inicializa torre 2 vacía
        self.__torre3 = PilaEncadenada()    # Inicializa torre 3 vacía
        self.__jugadas = 0                  # Contador de jugadas realizadas

        # Estado inicial: todos los discos en torre 1 (de n a 1, el más grande abajo)
        # Para cada disco desde n hasta 1 de uno en uno hacia atrás… el cero es valor final exclusivo
        for disco in range(n, 0, -1):
            self.__torre1.insertar(disco)  # Inserta cada disco en la torre 1, de mayor a menor

    # ---------- Helpers privados ----------
    def __torre_por_num(self, num):
        # Devuelve la pila correspondiente al número de torre
        if num == 1: return self.__torre1
        if num == 2: return self.__torre2
        if num == 3: return self.__torre3
        return None

    def __ver_tope(self, pila):
        """Devuelve el valor del tope sin modificar la pila (peek)."""
        if pila.vacia():
            return None                    # Si la pila está vacía, devuelve None
        x = pila.suprimir()                # Saca el tope
        pila.insertar(x)                   # Lo vuelve a insertar para no modificar la pila
        return x                           # Devuelve el valor del tope

    def __estado_final(self):
        """Comprueba si el juego terminó (todo en torre 3)."""
        return self.__torre1.vacia() and self.__torre2.vacia()

    def __imprimir_estado(self):
        print("\n=== Estado de las torres (tope → base) ===")
        print("Torre 1:")
        self.__torre1.recorrer()           # Muestra los discos de la torre 1
        print("Torre 2:")
        self.__torre2.recorrer()           # Muestra los discos de la torre 2
        print("Torre 3:")
        self.__torre3.recorrer()           # Muestra los discos de la torre 3
        print("==========================================\n")

    def __mover_si_valido(self, origen_num, destino_num):
        """Intenta mover un disco; valida reglas. Devuelve (ok, mensaje)."""
        if origen_num == destino_num:
            return False, "Origen y destino no pueden ser la misma torre."

        origen = self.__torre_por_num(origen_num)   # Obtiene la torre de origen
        destino = self.__torre_por_num(destino_num) # Obtiene la torre de destino

        if origen is None or destino is None:
            return False, "Las torres válidas son 1, 2 y 3."

        if origen.vacia():
            return False, f"La torre {origen_num} está vacía."

        disco = origen.suprimir()                     # Saca el disco del tope de origen

        tope_destino = self.__ver_tope(destino)      # Consulta el tope de la torre destino
        if tope_destino is not None and tope_destino < disco:
            # Si el disco es más grande que el tope destino, movimiento inválido
            origen.insertar(disco)                  # Devuelve el disco a la torre original
            return False, f"No se puede colocar el disco {disco} sobre {tope_destino}."

        destino.insertar(disco)                      # Inserta disco en torre destino
        self.__jugadas += 1                          # Aumenta contador de jugadas
        return True, f"Moviste el disco {disco} de la torre {origen_num} a la torre {destino_num}."

    # ---------- Modo de juego interactivo ----------
    def jugar(self):
        print(f"\n¡Bienvenid@ a Torres de Hanoi! Discos: {self.__n}")
        self.__imprimir_estado()                     # Muestra estado inicial
        minimo = (1 << self.__n) - 1                # Calcula jugadas mínimas: 2**n - 1

        while not self.__estado_final():            # Mientras el juego no haya terminado
            entrada = input("Ingresá 'origen destino' (ej: 1 3) o 'q' para salir: ").strip()
            if entrada.lower() == 'q':
                print("Juego cancelado por el usuario.")
                return

            partes = entrada.split()                # Separa los números ingresados
            if len(partes) != 2:
                print("Entrada inválida. Formato esperado: dos números (1..3).")
                continue

            try:
                origen_num = int(partes[0])       # Convierte a entero origen
                destino_num = int(partes[1])      # Convierte a entero destino
            except ValueError:
                print("Entrada inválida. Deben ser números enteros 1..3.")
                continue

            ok, msg = self.__mover_si_valido(origen_num, destino_num)  # Intenta mover
            print(msg)                              # Muestra mensaje de éxito o error
            self.__imprimir_estado()                # Muestra el estado actualizado

        print(f"¡Felicitaciones! Terminaste en {self.__jugadas} jugadas.")
        print(f"El mínimo teórico es {minimo} jugadas (2^n - 1).")


# ================== MAIN ==================
if __name__ == "__main__":
    try:
        n = int(input("Ingresá el número de discos (n > 0): "))  # Solicita cantidad de discos
        if n <= 0:
            print("El número de discos debe ser mayor que cero.")
        else:
            juego = TorresdeHanoi(n)      # Crea instancia del juego
            juego.jugar()                  # Inicia modo interactivo
    except ValueError:
        print("Entrada inválida. Debe ser un número entero.")
# 3 discos
# Mover disco 1 de torre 1 → 3

# Mover disco 2 de torre 1 → 2

# Mover disco 1 de torre 3 → 2

# Mover disco 3 de torre 1 → 3

# Mover disco 1 de torre 2 → 1

# Mover disco 2 de torre 2 → 3

# Mover disco 1 de torre 1 → 3


# 4 discos
# Disco 1: 1 → 2

# Disco 2: 1 → 3

# Disco 1: 2 → 3

# Disco 3: 1 → 2

# Disco 1: 3 → 1

# Disco 2: 3 → 2

# Disco 1: 1 → 2

# Disco 4: 1 → 3

# Disco 1: 2 → 3

# Disco 2: 2 → 1

# Disco 1: 3 → 1

# Disco 3: 2 → 3

# Disco 1: 1 → 2

# Disco 2: 1 → 3

# Disco 1: 2 → 3

# from claseNodo import Nodo
# from pilaEncadenada import PilaEncadenada

# class TorresdeHanoi:
#     def __init__(self, n):
#         self.__n = n
#         self.__torre1 = PilaEncadenada()
#         self.__torre2 = PilaEncadenada()
#         self.__torre3 = PilaEncadenada()
        
#         # Cargo la torre 1 con los discos (de mayor a menor)
#         for i in range(n, 0, -1):   # n, n-1, ..., 1
#             self.__torre1.insertar(i)

#     def mover(self, origen, destino):
#         """Mueve un disco desde la torre origen a la torre destino."""
#         if origen.estaVacia():
#             raise Exception("No se puede mover desde una torre vacía")
        
#         disco = origen.suprimir()
        
#         if not destino.estaVacia() and destino.tope() < disco:
#             # No se puede colocar un disco más grande sobre uno más chico
#             origen.insertar(disco)  # devolverlo a su lugar
#             raise Exception("Movimiento inválido")
        
#         destino.insertar(disco)

#     def resolver(self, n, origen, auxiliar, destino):
#         """Resuelve el problema recursivamente."""
#         if n == 1:
#             self.mover(origen, destino)
#         else:
#             self.resolver(n-1, origen, destino, auxiliar)
#             self.mover(origen, destino)
#             self.resolver(n-1, auxiliar, origen, destino)

#     def jugar(self):
#         """Ejecuta la solución del problema de Torres de Hanoi."""
#         self.resolver(self.__n, self.__torre1, self.__torre2, self.__torre3)

#     def mostrarTorres(self):
#         """Muestra el contenido de las 3 torres."""
#         print("Torre 1:", self.__torre1)
#         print("Torre 2:", self.__torre2)
#         print("Torre 3:", self.__torre3)


# hanoi = TorresdeHanoi(3)
# hanoi.mostrarTorres()
# hanoi.jugar()
# hanoi.mostrarTorres()
