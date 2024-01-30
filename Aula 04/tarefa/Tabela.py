from Linha import Linha
import json

class Tabela:
    def __init__(self, arquivo = None):
      self.cabecalho = Linha()
      self.dados = []
      if arquivo:
        file = open(arquivo, "r", encoding="utf8")
        i = 0
        for linha in file.readlines():
            converted_linha = json.loads(linha.replace("\n", "").replace("'", '"'))
            i += 1
            if i == 1:
              for c in converted_linha:
                self.add_cabecalho(c)
            else:
               self.addLinha(converted_linha)
        file.close()

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
      self.dados = sorted(self.dados, key=lambda linha: linha[posicao])

    def writeFile(self, arquivo):
      file = open(arquivo, "w", encoding="utf8")
      file.write(str(self.cabecalho) + "\n")
      file.close()
      file = open(arquivo, "a", encoding="utf8")
      for d in self.dados:
        file.write(str(d) + "\n")
      file.close()
      