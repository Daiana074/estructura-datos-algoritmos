import random
from colaSecuencial import ColaSecuencial

class SimulacionImpresora:

    def __init__(self, duracion=60):
        self.duracion = duracion              # minutos totales
        self.velocidad = 10                   # páginas por minuto
        self.tiempo_max = 3                   # minutos por trabajo
        self.trabajos_atendidos = 0
        self.trabajos_sin_atender = 0
        self.tiempo_espera_total = 0
        self.cola = ColaSecuencial()

    def generar_trabajo(self, tiempo_actual):
        paginas = random.randint(1, 100)   # aleatorio entre 1 y 100
        # Guardamos (paginas_restantes, tiempo_llegada)
        self.cola.insertar((paginas, tiempo_actual))

    def ejecutar(self):
        for minuto in range(self.duracion + 1):  # desde 0 hasta 60
            # Cada 5 minutos llega un trabajo nuevo
            if minuto % 5 == 0:
                self.generar_trabajo(minuto)

            # Si hay trabajos, procesar uno
            if not self.cola.vacia():
                paginas, llegada = self.cola.suprimir()

                # tiempo de espera = minuto actual - llegada
                espera = minuto - llegada

                # La impresora puede procesar hasta 30 páginas en 3 min
                paginas_procesadas = min(paginas, self.velocidad * self.tiempo_max)

                if paginas <= paginas_procesadas:
                    # El trabajo se termina
                    self.trabajos_atendidos += 1
                    self.tiempo_espera_total += espera
                else:
                    # Le quedan páginas → se vuelve a la cola
                    self.cola.insertar((paginas - paginas_procesadas, minuto))

        # Al finalizar la simulación
        self.trabajos_sin_atender = self.contar_restantes()

    def contar_restantes(self):
        cont = 0
        while not self.cola.vacia():
            self.cola.suprimir()
            cont += 1
        return cont

    def resultados(self):
        print("Resultados de la simulación de 1 hora:")
        print(f"a) Trabajos sin atender: {self.trabajos_sin_atender}")
        if self.trabajos_atendidos > 0:
            prom_espera = self.tiempo_espera_total / self.trabajos_atendidos
        else:
            prom_espera = 0
        print(f"b) Promedio de espera de trabajos atendidos: {prom_espera:.2f} minutos")


# Ejemplo de uso
if __name__ == "__main__":
    sim = SimulacionImpresora()
    sim.ejecutar()
    sim.resultados()
