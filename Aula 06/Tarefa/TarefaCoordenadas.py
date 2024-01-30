# Tarefa em grupo de 3 pessoas. Apenas um submete, porém com o nome
# dos três integrantes.
# Marcelli Roberta Sarti - 247549
# Wallyson Jhonatan de Oliveira - 247616

from classes import BancoDeDados
from PIL import Image, ImageDraw

# Neste projeto, você deve inicialmente abrir o arquivo de coordenadas.
# Em seguida, você deve fazer a varredura nas coordenadas.
bancodedados = BancoDeDados("coordenadas.txt")

# Depois disso, você deve criar uma imagem em branco, 1001x1001.
img = Image.new('RGB',(1001,1001),(255,255,255))
draw = ImageDraw.Draw(img)
# img.show()

# Cada coordenada do arquivo deve ser desenhada na imagem que foi
# criada.
#
# Você deve fazer um processo de normalização de modo que a menor latitude
# esteja associada à posição zero e a maior latitude esteja associada à posição
# 1000. Uma latitude intermediaria vai estar em um ponto intemediario entre
# 0 e 1000. Este é um processo chamado normalização.
latitude_min, latitude_max = bancodedados.getLatitudeMinMax()

# O mesmo deve ser feito para longitude.
longitute_min, longitute_max = bancodedados.getLongitudeMinMax()

# Desenha as coordenadas na imagem
coordenadas = bancodedados.getCoordernadas()

fronteiras = []
for coor in coordenadas:

    latitude = float(coor[0])
    longitude = float(coor[1])
    latitude_norm = int((latitude - latitude_min) / (latitude_max - latitude_min) * 1000)
    longitude_norm = int((longitude - longitute_min) / (longitute_max - longitute_min) * 1000)

    if (latitude_norm == 0) or (latitude_norm == 1000) or (longitude_norm == 0) or (longitude_norm == 100):
        fronteiras.append(coor[2]) 
    # Uma melhoria que deve ser feita é a seguinte: Cada estado
    # deve ser pintado com uma cor entre (preto, azul, amarelo, cinza).
    
    # ESTADOS DA REGIÃO NORTE
    if coor[2] in ['AC', 'AM', 'AP', 'PA', 'RO', 'RR', 'TO']:
        cor = 'black'
    # ESTADOS DA REGIÃO NORDESTE
    elif coor[2] in ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']:
        cor = 'yellow'
    # ESTADOS DA REGIÃO CENTRO-OESTE
    elif coor[2] in ['DF', 'GO', 'MT', 'MS']:
        cor = 'blue'
    # ESTADOS DA REGIÃO SUL/SUDESTE
    else:
        cor = 'grey'

    # Além disso, estados que possuem fronteira maior que zero
    # devem ter cores diferentes.
    if coor[2] in fronteiras:
        cor = 'red'

    draw.point((latitude_norm, longitude_norm), fill=cor)

# Após desenhar as coordenadas na imagem, deve rotacioná-la de maneira
# que o norte esteja para cima e o leste para a direita.
img = img.rotate(90, expand=True)
img.show()

# Ao final, você deve salvar o resulado em Brasil.png
img.save("Brasil.png")

# Você deve submeter o arquivo Brasil.png e o arquivo python com o programa.


