class Livro:
    def __init__(self, titulo, ano_publicacao, numero_paginas):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.numero_paginas = numero_paginas

    def __str__(self):
        return "Título: " + self.titulo + ". Ano de publicação: " + self.ano_publicacao + ". Número de páginas: " + self.numero_paginas
        
    def get_titulo(self):
        return self.titulo


livro1 = Livro("Livro 1", "2023", "600")
print(livro1)

livro2 = Livro("Livro 2", "2022", "500")
print(livro2)

livro3 = Livro("Livro 3", "2021", "400")
print(livro3)

livro4 = Livro("Livro 4", "2020", "300")
print(livro4)

livro5 = Livro("Livro 5", "2019", "200")
print(livro3)

livro6 = Livro("Livro 6", "2018", "100")
print(livro4)

class Biblioteca:
    def __init__(self, nome):
       self.nome = nome
       self.livros = []
    
    def append(self, livro: Livro):
        self.livros.append(livro)

    def __str__(self):
        str_livros = "Livros da biblioteca " + self.nome + ":\n"
        for i in self.livros:
            str_livros += i.get_titulo() + "\n"
      
        return str_livros
    
    def interseccao(self, biblioteca):
        interseccao = []
        for i in self.livros:
            for j in biblioteca.livros:
                if i.titulo == j.titulo and i.ano_publicacao == j.ano_publicacao and i.numero_paginas == j.numero_paginas:
                    interseccao.append(str(i))

        return interseccao
    
bc = Biblioteca("BC")
bc.append(livro1)
bc.append(livro2)
bc.append(livro3)
bc.append(livro4)

print(bc)

cotil = Biblioteca("Cotil")
cotil.append(livro3)
cotil.append(livro4)
cotil.append(livro5)
cotil.append(livro6)

print(cotil)

print(cotil.interseccao(bc))