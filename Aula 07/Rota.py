# Marcelli Roberta Sarti 247549
# Wallyson Jhonatan de Oliveira 247616

from Coordenada import Coordenada
import random

class Rota():
    def __init__(self):
        self.lista = []

    def addCoord(self, coordenada: Coordenada):
        self.lista.append(coordenada)

    def __str__(self):
        string = ""
        cont = 0
        for itens in self.lista:
            cont += 1
            string += str(itens) + '->'
            
            if cont == len(self.lista):
                string += str(self.lista[0])
        
        return string
    
    def comprimento(self):
        distancia = 0
        cont = 0
        primeiro_item = None
        for itens in self.lista:
            cont += 1
            
            if primeiro_item is not None:
                distancia += primeiro_item.distancia(itens)
            primeiro_item = itens
            if cont == len(self.lista):
                distancia += primeiro_item.distancia(self.lista[0])

        return distancia
            
    def copy(self):
        rota = Rota()
        for itens in self.lista:
            rota.addCoord(itens)
        return rota
    
    def shuffle(self):
        random.shuffle(self.lista)

    def otimiza(self):
        # # Você deve melhorar esta função. Fazer otimizar mais rápido.
        for _ in range(100000):
            # Escolhe dois índices aleatórios diferentes
            i, j = random.sample(range(len(self.lista)), 2)

            # Faz uma cópia da rota atual
            rota_aux = self.copy()
            
            # Troca as coordenadas nas posições i e j
            rota_aux.lista[i], rota_aux.lista[j] = rota_aux.lista[j], rota_aux.lista[i]
            
            # Se a nova rota for mais curta ou por uma probabilidade aleatória, aceita a troca
            if rota_aux.comprimento() < self.comprimento():
                print(self.comprimento())
                self = rota_aux
        
        return self