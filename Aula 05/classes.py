import geopy.distance

class Cidade:
    def __init__(self, cidade, estado, sigla, latitude, longitude):
        self.cidade = cidade
        self.estado = estado
        self.sigla = sigla
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):
        return self.cidade+";"+self.estado+";"+self.sigla+";"+str(self.latitude)+";"+str(self.longitude)

class BancoDeDados:
    def __init__(self, arquivo):
        self.cidades = []
        if arquivo:
            file = open(arquivo, "r")
            for f in file.readlines():
                info = f.replace("\n", "").split(";")
                cidade = info[0]
                estado = info[1]
                sigla = info[2]
                latitude = info[3]
                longitude = info[4]
                self.cidades.append(Cidade(cidade, estado, sigla, latitude, longitude))

    def maisproximo(self, latitude, longitude):
        menor_distancia = 100000000
        menor_distancia_cidade = ""
        for dado in self.cidades:
            dist = geopy.distance.geodesic((dado.latitude, dado.longitude), (latitude, longitude)).km
            if dist < menor_distancia and dist != 0:
                menor_distancia = dist
                menor_distancia_cidade = dado
        
        return menor_distancia_cidade, menor_distancia
    

bancodedados = BancoDeDados("coordenadas.txt")
latitude = float(input("Digite a latitude: "))
longitude = float(input("Digite a longitude:"))
# latitude = -22.9
# longitude = -47.0833333
cidade, km = bancodedados.maisproximo(latitude, longitude)
print(f"A coordenada mais próxima de ({str(latitude)}, {str(longitude)}) é:")
print(cidade)
print("Distância:"+str(km))