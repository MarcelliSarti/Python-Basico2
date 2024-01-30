# Marcelli Roberta Sarti 247549
# Wallyson Jhonatan de Oliveira 247616

from Coordenada import Coordenada
from PIL import Image, ImageDraw
import random
import time

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
                self.lista = rota_aux.lista

    def espera(self, t):
        tin = time.time()
        delta = 0 
        
        while delta < t:
            delta = int(time.time() - tin)
            
            if delta % 1000 == 0 and delta != 0:
                print(f'Esperando: {delta}')

    def randomCoords(self, n, max_coord):
        self.lista = []

        for i in range(n):
            x = random.randint(1, max_coord)
            y = random.randint(1, max_coord)
            coord = Coordenada((x, y))
            self.addCoord(coord)

    def maximo(self):
        max_x = 0
        max_y = 0
        for coord in self.lista:
            lat = coord.get()[0]
            lon = coord.get()[1]
            if lat > max_x:
                max_x = lat
            if lon > max_y:
                max_y = lon
        
        return (max_x, max_y)

    def desenha(self, filename):
        max_x = self.maximo()[0]
        max_y = self.maximo()[1]
    
        imagem = Image.new('RGB', (max_x + 20, max_y + 50), color='white')
        desenho = ImageDraw.Draw(imagem)

        for i in range(len(self.lista)-1):
            a = (self.lista[i].get()[0] + 10, self.lista[i].get()[1] + 10)
            b = (self.lista[i+1].get()[0] + 10, self.lista[i+1].get()[1] + 10)
            desenho.line([a, b], fill='black', width=4)

        # Conecta a última coordenada com a primeira
        a = (self.lista[-1].get()[0] + 10, self.lista[-1].get()[1] + 10)
        b = (self.lista[0].get()[0] + 10, self.lista[0].get()[1] + 10)
        desenho.line([a, b], fill='black', width=4)

        comprimento = self.comprimento()
        desenho.text((10, max_y + 20), f'Custo: {comprimento}', fill='black')

        imagem.save(filename)
        return imagem

