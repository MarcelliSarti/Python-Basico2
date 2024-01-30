from Tabela import Tabela
import pandas as pd
import json

class TabelaBD(Tabela):
    def conta(self, coluna):
        df = pd.DataFrame(self.dados, columns=json.loads(str(self.cabecalho).replace("'", '"')))
        df_count = df[coluna].value_counts().sort_values(ascending=True).reset_index()

        tabela_count = Tabela()
        tabela_count.add_cabecalho(coluna)
        tabela_count.add_cabecalho("numero")
        for linha in df_count.values.tolist():
            tabela_count.addLinha(linha)

        return tabela_count
    
    def select(self, coluna, valor):
        colunas = json.loads(str(self.cabecalho).replace("'", '"'))
        df = pd.DataFrame(self.dados, columns=colunas)
        df_selected = (df[df[coluna] == valor])

        tabela_selected = Tabela()
        for c in colunas:
            tabela_selected.add_cabecalho(c)

        for d in df_selected.values.tolist():
            tabela_selected.addLinha(d)

        return tabela_selected
