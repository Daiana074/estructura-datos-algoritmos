#from claseNodo import Nodo
from colaEncadenada import ColaEncadenada
import random

class SimulacionBanco:
    __duracion:int
    __tiemposCajeros:list
    __colas:list
    __tiempoCajeros:list
    __maxEspera:int
    __clientesAtendidos:int
    __clientesSinAtender:int
    __totalEsperaAtendidos:int
    __totalEsperaNoAtendidos:int

    def __init__(self, duracion=120):
        self.__duracion = duracion                # minutos de simulación (2 horas)
        self.__tiemposCajeros = [5, 3, 4]         # tiempos de servicio de los 3 cajeros
        self.__colas = [ColaEncadenada(), ColaEncadenada(), ColaEncadenada()]
        self.__tiempoCajeros = [0, 0, 0]          # tiempo restante de cada cajero

        # estadísticas
        self.__maxEspera = 0
        self.__clientesAtendidos = 0
        self.__clientesSinAtender = 0
        self.__totalEsperaAtendidos = 0
        self.__totalEsperaNoAtendidos = 0

        # Ejecutamos la simulación automáticamente
        self.__ejecutar()
        self.__resultados()

    def __llegadaCliente(self, minuto:int):
        """Genera la llegada de un cliente y lo ubica en una cola."""
        libres = [i for i in range(3) if self.__tiempoCajeros[i] == 0 and self.__colas[i].vacia()]
        if libres:
            cajero = random.choice(libres)
            self.__colas[cajero].insertar((minuto, 0))
        else:
            longitudes = [self.__longitudCola(c) for c in self.__colas]
            min_len = min(longitudes)
            indices = [i for i, l in enumerate(longitudes) if l == min_len]
            cajero = random.choice(indices)
            self.__colas[cajero].insertar((minuto, 0))

    def __longitudCola(self, cola:ColaEncadenada)->int:
        cont = 0
        aux = cola._ColaEncadenada__pri
        while aux is not None:
            cont += 1
            aux = aux.getSiguiente()
        return cont

    def __ejecutar(self):
        for minuto in range(self.__duracion + 1):
            # Llegada de clientes cada 2 minutos
            if minuto % 2 == 0:
                self.__llegadaCliente(minuto)

            # Procesamiento de cajeros
            for i in range(3):
                if self.__tiempoCajeros[i] > 0:
                    self.__tiempoCajeros[i] -= 1
                else:
                    if not self.__colas[i].vacia():
                        llegada, espera = self.__colas[i].suprimir()
                        tiempo_espera = minuto - llegada
                        self.__maxEspera = max(self.__maxEspera, tiempo_espera)
                        self.__totalEsperaAtendidos += tiempo_espera
                        self.__clientesAtendidos += 1
                        self.__tiempoCajeros[i] = self.__tiemposCajeros[i]

        # Al terminar, calcular los que quedaron sin atender
        for i in range(3):
            while not self.__colas[i].vacia():
                llegada, espera = self.__colas[i].suprimir()
                tiempo_espera = self.__duracion - llegada
                self.__clientesSinAtender += 1
                self.__totalEsperaNoAtendidos += tiempo_espera

    def __resultados(self):
        print("Resultados de la simulación del banco (2 horas):")
        print(f"a) Tiempo máximo de espera: {self.__maxEspera} minutos")
        print(f"b) Clientes atendidos: {self.__clientesAtendidos}")
        print(f"c) Clientes sin atender: {self.__clientesSinAtender}")
        prom_atendidos = (self.__totalEsperaAtendidos / self.__clientesAtendidos) if self.__clientesAtendidos else 0
        prom_no_atendidos = (self.__totalEsperaNoAtendidos / self.__clientesSinAtender) if self.__clientesSinAtender else 0
        print(f"d) Promedio de espera (atendidos): {prom_atendidos:.2f} minutos")
        print(f"e) Promedio de espera (no atendidos): {prom_no_atendidos:.2f} minutos")


# Ejemplo de uso:
simulacion = SimulacionBanco()
