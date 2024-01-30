class Cidade:
    def __init__(self, cidade, estado, sigla, latitude, longitude):
        self.cidade = cidade
        self.estado = estado
        self.sigla = sigla
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):
        # return [self.cidade, self.estado, self.sigla, self.latitude, self.longitude]
        return self.cidade+";"+self.estado+";"+self.sigla+";"+str(self.latitude)+";"+str(self.longitude)
    
    def getLatitude(self):
        return self.latitude
    
    def getLongitude(self):
        return self.longitude
    
    def getSigla(self):
        return self.sigla

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

    def __str__(self):
        for cidade in self.cidades:
            print(cidade)

    def getLatitudeMinMax(self):
        latitudes = []
        for cidade in self.cidades:
            latitudes.append(cidade.getLatitude()) 

        return min(latitudes), max(latitudes)

    def getLongitudeMinMax(self):
        longitudes = []
        for cidade in self.cidades:
            longitudes.append(cidade.getLongitude()) 

        return min(longitudes), max(longitudes)
    
    def getCoordernadas(self):
        coordernadas = []
        for cidade in self.cidades:
            coordernadas.append((cidade.getLatitude(), cidade.getLongitude(), cidade.getSigla())) 

        return coordernadas
