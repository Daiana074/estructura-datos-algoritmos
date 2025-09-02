class Escaleras(object):
    
    def __init__(self, n=0):
        self.__subir(n)
        

    def subir(self, n, resParcial=""):
        if n==0: #problema resuelto, escribo salida
            print(resParcial)
            return 1
        res = 0
        if n>=1: #podemos subir un escalon
            self.subir(n-1, resParcial+" 1")
            res += 1
        if n>=2: #podemos subir dos escalones
            self.subir(n-2, resParcial+" 2")
            res += 1
        return res  


escalera=Escaleras(5)
