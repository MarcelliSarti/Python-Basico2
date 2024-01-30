from Linha import Linha

class Tabela:
    def __init__(self):
      self.cabecalho = Linha()
      self.dados = []

    def add_cabecalho(self, valor):
      self.cabecalho.append(valor)

    def addLinha(self, linha):
      if len(linha) != len(self.cabecalho):
          print("tamanho da linha incompatível")
      else:
          self.dados.append(linha)

    def __str__(self):
      returned_string = str(self.cabecalho) + "\n"
      returned_string += "--------------------------------------- \n" 
      for i in range(len(self.dados)):
        returned_string += str(self.dados[i]) + "\n"
      return returned_string
    
    def ordena_por(self, valor):
      posicao = self.cabecalho.posicao(valor)
      self.dados = sorted(self.dados, key=lambda linha: linha.dados[posicao])
      