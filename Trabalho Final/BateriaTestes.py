from Otimizador import Otimizador
import matplotlib.pyplot as plt
from Rota import Rota
import numpy as np


# Marcelli Roberta Sarti 247549
# Wallyson Jhonatan de Oliveira 247616


class BateriaTestes:
    funcoes = []

    def addFuncao(self, funcao, nome):
        self.funcoes.append((funcao, nome))


    ''''
    Em grupo de 3 pessoas. Apenas uma envia o arquivo no moodle. Nome dos 
    três integrantes dentro do arquivo.
    Você deve fazer primeiro a tarefa descrita na Aula 9/10 e depois resolver
    esta tarefa (aula 11).
    
    Primeiramente deve ser cadastrado um conjunto de funções de otimização na classe
    BateriaTestes, através do método addFunção.
    
    A próxima função, chamada 'executa', recebe
    o número de repetições que pode ser 3, 5 ou 10 por exemplo. O tempo, em ms, e uma 
    lista de tamanhos. Por exemplo, se a lista de tamanhos for [10,100,100], deve-se executar
    as funções para rotas de tamanho 10, 1000 e 1000. Deve ser criada uma única instância (rota) 
    para ser otimizada para cada valor distinto em sizeList. No caso de sizeList for [10,100,1000],
    devem ser criadas 3 rotas, uma com 10, uma com 100 e uma com 1000 coordenadas.
    A rota deve ser otimizada por cada uma das funções. Além disso, deve-se repetir a otimização
    'n_repeticoes' vezes. Por exemplo se n_repeticoes=10, deve-se executar a função de otimização
    10 vezes e calcular a média e o desvio padrão. Uma vez que todos estes dados foram calculados,
    deve ser criado um gráfico igual ao disponível em 'Bateria.png'. 
    A média é o comprimento da barra e o desvio padrão é o erro que está no topo da barra.
    Note que, se sizeList for 
    alterado para mais ou para menos valores, o gráfico deve ser criado automaticamente para o 
    novo conjunto sizeList. Também se forem adicionadas ou removidas funções em self.funções, o 
    gráfico deve continuar executando de maneira automática.
    A bateria de testes executa 'n_repeticoes' vezes para cada par funcao X tamanho.
    Deve ser criado um gráfico para cada size em sizeList. Por exemplo, se sizeList for [10,100,1000]
    deve ser criado um gráfico Otimizacao_10.png, Otimizaca_100.png e Otimizacao_1000.png. No gráfico
    Otimização_10.png deve ficar a primeira execução de cada função em instâncias de tamanho 10. 
    O mesmo para size 100 e 1000. Veja Os gráficos Otimização_X.png para ter um exemplo. 
    
    No lugar de 'Grupo 1'
    # deve estar um nome curto que identifique o seu grupo. O nome deve
    # ser composto de um nome dos integrantes. Exemplo:
    # Rodrigo_Ivan_Celso. Além disso, o arquivo Phyton deve seguir o mesmo padrão.
    # BateriaTestes_Rodrigo_Ivan_Celso.py.
    '''

    def gera_grafico_bateria(self, resultados, labels, sizes):
        width = 0.2  # Largura das barras
        x = np.arange(len(sizes))  # Posições no eixo x para os tamanhos

        for i, func_label in enumerate(labels):
            valores_media = [resultados[func_label][size]['media'] for size in sizes]
            desvio_padrao = [resultados[func_label][size]['desvio_padrao'] for size in sizes]

            plt.bar(x + i * width, valores_media, width, label=f"{func_label}", yerr=desvio_padrao)

        plt.xlabel('Tamanho Rota')
        plt.ylabel('Custo')
        plt.xticks(x + width * (len(labels) - 1) / 2, sizes)
        plt.legend()
        plt.savefig('Bateria.png')
        # plt.show()
        plt.clf()

    def gera_grafico_otimizacao(self, resultados, labels, size):
        for label in labels:
            plt.plot(resultados[label]["tempo"], resultados[label]["comprimento"], label=label)

        # Adiciona rótulos e título
        plt.xlabel('Tempo (ms)')
        plt.ylabel('Comprimento (pixel)')
        plt.title('Comprimento versus Tempo (ms)')

        plt.tight_layout()
        plt.legend()
        # plt.show()
        plt.savefig(f"Otimizacao_{size}.png")
        plt.clf()

    def executa(self, n_repeticoes: int, tempo_ms, sizeList):
        # Criar o gráfico de barras
        bateria = {}  # Dicionário para armazenar os resultados
        otimizador_graf = {}

        for size in sizeList:
            print(f"Criando Rota_"+str(size))
            rota = Rota()
            rota.randomCoords(size, 400)
            otimizador_graf[size] = {}

            for otimizador in self.funcoes:
                funcao = otimizador[0]
                comprimentos = []
                otimizador_graf[size][otimizador[1]] = {"comprimento": [], "tempo": []}


                for rep in range(n_repeticoes):
                    print(f"Repetição {rep} da função {otimizador[1]} com "+str(size)+" vertices")
                    tempo, comp = funcao(rota, tempo_ms)
                    comprimentos.append(rota.comprimento())

                    if rep == 0:
                        otimizador_graf[size][otimizador[1]]["comprimento"] = comp
                        otimizador_graf[size][otimizador[1]]["tempo"] = tempo

                media = np.mean(comprimentos)
                desvio_padrao = np.std(comprimentos)

                if otimizador[1] not in bateria: # Se o otimizador ainda nao estiver no dict, cria
                    bateria[otimizador[1]] = {}
                if size not in bateria[otimizador[1]]: # Se o tamanho em questão ainda não eestiver no dict, cria
                    bateria[otimizador[1]][size] = {'media': None, 'desvio_padrao': None}

                # Adiciona valores de media e desvio padrão para plotar o gráfico bateria, posteriormente
                bateria[otimizador[1]][size]['media'] = media
                bateria[otimizador[1]][size]['desvio_padrao'] = desvio_padrao

            self.gera_grafico_otimizacao(otimizador_graf[size], [ot[1] for ot in self.funcoes], size)
                
        labels = [otimizador[1] for otimizador in self.funcoes]
        self.gera_grafico_bateria(bateria, labels, sizeList)

'''
Esta parte do código cria uma bateria de teste, cadastra as funções
e executa a bateria de testes. Esta parte não deve ser alterada.
Note que ao adicionar uma função também é passado um nome (rótulo) 
para a funcão. Todo o resto deve acontecer dentro da função executa.
'''
bt = BateriaTestes()
otimizador = Otimizador()
bt.addFuncao(otimizador.singleSwap, "singleSwap")
bt.addFuncao(otimizador.aleatorio, "aleatorio")
bt.addFuncao(otimizador.otimizadorGrupoMarcelliWallyson, "otimizadorGrupoMarcelliWallyson")
# descomentar a linha abaixo e refazer a bateria de testes.
bt.addFuncao(otimizador.singleSwap, "singleSwap_B")
bt.addFuncao(otimizador.aleatorio, "aleatorio_B")
bt.addFuncao(otimizador.otimizadorGrupoMarcelliWallyson, "otimizadorGrupoMarcelliWallyson_B")



tempo_ms = 1000
repeticoes = 3
size = [10,50,100,200,300,500,600]
#descomentar a linha abaixo e refazer a bateria de testes
#size = [10,100,1000]
bt.executa(repeticoes, tempo_ms, size)

