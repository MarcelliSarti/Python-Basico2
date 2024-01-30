import random
from Rota import Rota
import time
from matplotlib import pyplot

# Ainda não é para entregar. Em grupo de 3 pessoas.
# Marcelli Roberta Sarti 247549
# Wallyson Jhonatan de Oliveira 247616
# Vai ser pedido para entregar futuramente, junto
# com o conteúdo das proximas aulas.


class Otimizador:
    # Este é o construtor do otimizador. Você pode adicionar código aqui
    # se julgar necessário.
    def __init__(self):
        self.plt = pyplot
        self.tempo_swap = []
        self.comp_swap = []
        self.tempo_alet = []
        self.comp_alet = []
        self.tempo_otim = []
        self.comp_otim = []

    # Este método de otimização já está implementado.
    # Toda vez que o comprimento for atualizado para um valor menor, é
    # necessário salvar o comprimento e o tempo gasto na função
    # para fazer o gráfico.
    # Ao final da execução, é necessário usar o matplotlib (pyplot)
    # para gerar o gráfico (comprimento X tempo).
    # Deve ser feito o mesmo para a função de otimização 'aleatório'
    # e 'otimizadorGrupo1'
    # As três séries temporais devem ser salvas em um mesmo gráfico,
    # conforme figuras 'Resultado_10x.py'
    # Seu grupo pode adicionar código nesta função se julgar necessário.
    # O mesmo para os outros dois otimizadores.
    # A linha do gráfico referente ao 'SingleSwap' deve estar em preto.
    # A linha do gráfico referente ao 'Aleatório' deve estar em verde.
    # A linha do gráfico referente ao 'otimizadorGrupo1' deve estar em azul
    # e deve ser mais grossa que a linha dos outros algoritmos.
    # Todas as linhas devem iniciar no tempo zero e terminar no tempo final.
    def singleSwap(self, rota: Rota, time_ms: int):
        self.tempo_swap = []
        self.comp_swap = []
        # Inicia a partir de uma rota não otimizada
        rota.shuffle()
        # Tempo de entrada na função.
        tin = round(time.time() * 1000)
        # Tempo gasto na função.
        delta_ms = round(time.time() * 1000) - tin
        minComprimento = rota.comprimento()
        while delta_ms < time_ms:
            self.tempo_swap.append(delta_ms)
            self.comp_swap.append(minComprimento)
            # atualiza delta
            delta_ms = round(time.time() * 1000) - tin
            size_rota = len(rota.lista)
            pos1 = random.randrange(0, size_rota)
            pos2 = random.randrange(0, size_rota)
            swap(rota, pos1, pos2)
            if rota.comprimento() < minComprimento:
                minComprimento = rota.comprimento()
            else:
                # desfaz o swap
                swap(rota, pos1, pos2)

        return self.tempo_swap, self.comp_swap

    def aleatorio(self, rota: Rota, time_ms: int):
        self.tempo_alet = []
        self.comp_alet = []
        # inicia a partir de uma rota não otimizada
        rota.shuffle()
        tin = round(time.time() * 1000)
        delta_ms = round(time.time() * 1000) - tin
        minComprimento = rota.comprimento()
        while delta_ms < time_ms:
            self.tempo_alet.append(delta_ms)
            self.comp_alet.append(minComprimento)
            delta_ms = round(time.time() * 1000) - tin
            rotaAux = rota.copy()
            rotaAux.shuffle()
            if rotaAux.comprimento() < minComprimento:
                rota.lista = rotaAux.lista
                minComprimento = rota.comprimento()

        return self.tempo_alet, self.comp_alet

    # Aqui você deve usar sua criatividade e propor um algoritmo de
    # otimização. O algoritmo deixado é apenas um exemplo.
    # Ao fixar um label para o seu grupo
    # dê um nome para o seu grupo que o diferencie dos demais.
    # Veja a Figura Resultado_10x.png. No lugar de 'Algoritmo do Grupo 1'
    # deve estar um nome curto que identifique o seu grupo. O nome deve
    # ser composto de um nome dos integrantes. Exemplo:
    # Rodrigo_Ivan_Celso
    # Note que a linha gráfico deve começar no tempo 0 e terminar no tempo time_ms
    def otimizadorGrupoMarcelliWallyson(self, rota: Rota, time_ms: int):
        self.tempo_otim = []
        self.comp_otim = []
        # Você deve melhorar esta função. Fazer otimizar mais rápido
        # inicia a partir de uma rota não otimizada
        rota.shuffle()
        tin = round(time.time() * 1000)
        delta_ms = round(time.time() * 1000) - tin
        while delta_ms < time_ms:
            self.tempo_otim.append(delta_ms)
            self.comp_otim.append(rota.comprimento())
            delta_ms = round(time.time() * 1000) - tin
            # Escolhe dois índices aleatórios diferentes
            i, j = random.sample(range(len(rota.lista)), 2)
            # Faz uma cópia da rota atual
            rota_aux = rota.copy()
            # Troca as coordenadas nas posições i e j
            rota_aux.lista[i], rota_aux.lista[j] = rota_aux.lista[j], rota_aux.lista[i]
            # Se a nova rota for mais curta ou por uma probabilidade aleatória, aceita a troca
            if rota_aux.comprimento() < rota.comprimento():
                rota.lista = rota_aux.lista

        return self.tempo_otim, self.comp_otim

    # Esta função deve salvar o gráfico. A função não deve ser alterada.
    # O objetivo final é colocar vários algoritmos vindos de grupos diferentes
    # num mesmo gráfico e depois esta função irá salvar a solução com todos os gráficos.
    def salvaFigura(self, filename):
        self.plt.plot(self.tempo_swap, self.comp_swap, 'k', label='SingleSwap')
        self.plt.plot(self.tempo_alet, self.comp_alet, 'g', label='Aleatório')
        self.plt.plot(self.tempo_otim, self.comp_otim, 'b', label='marcelli_wallyson', linewidth=3)
        
        # Adiciona rótulos e título
        self.plt.xlabel('Tempo (ms)')
        self.plt.ylabel('Comprimento (pixel)')
        self.plt.title('Comprimento versus Tempo (ms)')

        self.plt.tight_layout()
        self.plt.legend()
        self.plt.savefig(filename)


def swap(rota: Rota, pos1: int, pos2: int):
    aux = rota.lista[pos1]
    rota.lista[pos1] = rota.lista[pos2]
    rota.lista[pos2] = aux


# # Cria uma rota Vazia.
# r = Rota()
# # Número de coordenadas da rota
# size = int(input("Digite o número de vértices:"))
# # valor máximo x e y para a coordenada
# r.randomCoords(size, 400)
# # Cria o otimizador
# opt = Otimizador()
# # Tempo de otimização em ms
# time_ms = int(input("Digite o tempo em ms:"))
# # Otimiza por single swap
# opt.singleSwap(r, time_ms)
# # Otimização aleatório
# opt.aleatorio(r, time_ms)
# # Otimização feita por seu grupo
# opt.otimizadorGrupoMarcelliWallyson(r, time_ms)
# opt.salvaFigura("Resultado_" + str(size) + ".png")
