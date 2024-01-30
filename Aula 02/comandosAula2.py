# Uso do For em python
# Exemplo: percorrendo as letras de uma string
for letra in "Minha String":
    print(letra)

# Percorrendo os ítens de uma lista
amigos = ["Joao", "Pedro", "Mateus"]
for amigo in amigos:
    print(amigo)


# exercício: Faça uma função que troca
# as vogais de uma string por 'g'.

def traduz(frase):
    traducao = ""
    for letra in frase:
        if letra in "AEIOUaeiou":
            if letra.isupper():
                traducao = traducao + "G"
            else:
                traducao = traducao + "g"
        else:
            traducao = traducao + letra
    return traducao


print(traduz("Amanda"))

# Arquivos em python
# abrindo um arquivo para leitura.
file = open("empregados.txt", "r")  # read
file.close()

# abrindo um arquivo para escrita
# Cuidado: zera o arquivo.
file = open("empregados2.txt", "w")
file.close()

# abrindo um arquivo para acrescentar
file = open("empregados.txt", "a")  # append
file.close()

# Verificando se o arquivo pode ser lido
file = open("empregados.txt", "r")  # read
print(file.readable())

# leitura do arquivo. Lendo todo o arquivo.
print("before")
print(file.read())
print("after")
file.close()

# Lendo por linhas
file = open("empregados.txt", "r")  # read
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

# Fazendo um for para ler todas as linhas
file = open("empregados.txt", "r")  # read
print("----")
linha = file.readline()
while linha:
    print(linha)
    linha = file.readline()
print(str(linha == ""))
file.close()

# Utilizando o método readlines(), que transforma cada linha
# em um elemento da lista
file = open("empregados.txt", "r")
# cria a lista
empregados = file.readlines()
print(empregados)
file.close()

# for percorrendo as linhas
file = open("empregados.txt", "r")  # read
for empregado in file.readlines():
    print(empregado)

# "Dicionário em Python"
dados = dict()
# A chave é o item da esquerda e o valor o item da direita.
dados = {"nome": "Pedro", "idade": 25}
print(dados)
dados["sexo"] = "M"
print(dados)
# trocando o valor da chave 'nome'
dados["nome"] = "Paulo"
print(dados)
# deletando uma chave, e o respectivo valor.
del dados["sexo"]
print(dados)

# Exemplo de dicionário
mes = {
    "Jan": "Janeiro",
    "Fev": "Fevereiro",
    "Mar": "Março",
    "Abr": "Abril",
    "Mai": "Maio",
    "Jun": "Junho",
    "Jul": "Julho",
    "Ago": "Agosto",
    "Set": "Setembro",
    "Out": "Outubro",
    "Nov": "Novembro",
    "Dez": "Dezembro",
    1: "Janeiro",
    2: "Fevereiro",
}

print(mes["Jan"])
print(mes.get("Fev"))
print(mes.get("Abc "))
print(mes.get("Abc ", "Chave inválida"))
# print(mes["abc"])
print(mes.get(1))
print(mes[1])
mes[3] = "Março"

print(mes)

del mes[1]
del mes[2]
del mes[3]

print(mes)

# acessando os valores do dicionário
print(mes.values())

for val in mes.values():
    print(val)

# acessando as chaves do dicionário
print(mes.keys())

for k in mes.keys():
    print(k)

# percorrendo as chaves e os valores de um dicionário.
for key, value in mes.items():
    print(f"mes[{key}]={value}")

# Utilização de um dicionário para modelar uma locadora
# de filmes. Cada filme é um dicionário.

filme = {}
print(filme)
filme["titulo"] = "Star Wars"
filme["ano"] = "1977"
filme["Diretor"] = "George Lucas"

for k, v in filme.items():
    print(f"o {k} é {v}")

# a locadora é uma lista
locadora = []
print(locadora)
locadora.append(filme)

filme = {"titulo": "Vingadores",
         "ano": "2012",
         "Diretor": "Jose Whedon"}
locadora.append(filme)

filme = {"titulo": "Matrix",
         "ano": "1999",
"Diretor": "Wachowski"}
locadora.append(filme)

print(locadora[0]["ano"])

print(locadora[2]["titulo"])

# Tupla
pessoa = ("Luis", "Meira")
# Lista
pessoa = ["Luis", "Meira"]
# Dicionário
pessoa = {"nome": "Luis", "sobrenome": "Meira"}

# Outro exemplo de uso de dicionário.
# Cada estado é um dicionário e o brasil é uma lista
# de estados. O dicionário contêm a unidade federativa,
# que é o nome do estado, e a sigla.
estado = dict()
brasil = list()

# corrija
for c in range(0, 3):
    estado['uf'] = str(input("Unidade Federativa:"))
    estado['sigla'] = str(input("Sigla:"))
    brasil.append(estado)

for e in brasil:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}")
    print()