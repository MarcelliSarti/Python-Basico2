import math

class Coordenada():
    def __init__(self, *args):
        if len(args) == 0:
            self.lat = 0
            self.lon = 0
        elif len(args) == 1:
            if type(args) != tuple:
                raise Exception("Parâmetro não é uma tupla")
            if (len(args[0]) != 2):
                raise Exception(f"Numero de argumentos errado: 2")
    
            if all(isinstance(i, (int, float)) for i in args[0]):
                self.lat, self.lon = args[0]
            else:
                raise Exception("Elemento da tupla não é int or float")

        else:
            raise Exception("número de parâmetros errado")
        
    def __str__(self):
        return "(" + str(self.lat) + ", " + str(self.lon) + ")"
    
    def distancia(self, coordenada):
        return math.sqrt((coordenada.lat - self.lat)**2 + (coordenada.lon - self.lon)**2)