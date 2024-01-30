# Tentativas de plágio serão punidas de maneira exemplar.

# Marcelli Roberta Sarti - 247549
# Wallyson Jhonatan de Oliveira - 247411
# alunos devem estar junto com o código fonte.

# Nesta tarefa você irá receber um conjunto de assinaturas de funções e terá que implementá-las.
# Primeiramente considere um carro formado por um dicionário da seguinte maneira:
import random
import json
import pandas as pd


carro = dict()
carro["placa"] = "BBB2B99"
carro["ano"] = 2022
carro["marca"] = "chevrolet"
carro["modelo"] = "onix"


#Considere também uma variável a seguir:


filename = "carros.txt"


# Daqui para frente não é permitida mais nenhuma variável fora das funções.
# Todas as variáveis devem estar nas funções.


# você está recebendo um projeto com a descrição das funções
# para você implementar. Implemente as funções conforme a descrição.


# Esta função recebe uma variável carro, converte numa
# string e faz um append no arquivo associado a filename.
# Ao final o arquivo deve ser fechado. Deve haver um carro
# por linha.
# Número estimado de linhas: 3 (é o número de linhas gasto pelo
# professor.
def addCarro(carro):
    # seu código vem aqui.
    file = open(filename, "a")
    file.write(str(carro) + "\n")
    file.close()


# Esta função abre o arquivo associado a filename
# e, para cada linha, cria um dicionário carro no
# mesmo padrão mostrado no início deste trabalho.
# Cada carro deve ser adicionado a uma lista, e,
# ao final, esta lista deve ser devolvida pela função.
# O arquivo deve ser fechado após a leitura.
# Número estimado de linhas: 8
def carregaCarros():
    # seu código vem aqui.
    carros_list = []
    file = open(filename, "r")
    for c in file.readlines():
        car = c.replace("\n", "").replace("'", '"')
        carros_list.append(json.loads(car))
    file.close()
    return carros_list


# Esta função verifica se a placa passada como
# parâmetro já existe na base de dados (arquivo salvo
# em filename). Primeiro deve ser feita a leitura de
# todos os carros fazendo uma chamada da função
# carregaCarros. Após isso, deve verificar se
# a placa passada como parâmetro já existe. Neste caso devolve True.
# Caso a placa não exista, devolve False.
# Número estimado de linhas: 6
def contemPlaca(placa):
    # seu código vem aqui.
    carros = carregaCarros()
    for c in carros:
        if c.get("placa") == placa:
            return True
    return False


# Esta função cria uma placa aleatória no padrão novo,
# LLLNLNN onde L é uma letra e N é um dígito. Deve ser usada
# a função random.choice. A geração da placa aleatória implica
# que todas as placas têm a mesma probabilidade de
# serem geradas. Após gerar uma placa aleatória, deve ser chamada a função
# contemPlaca. Se a placa já existir, o processo deve se repetir até
# que seja gerada uma plana nova (que ainda não pertence ao arquivo de dados)
# Numero estimado de Linhas: 14.
def placaAleatoria():
    # seu código vem aqui.
    alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    check_placa = True
    while(check_placa):
        placa_aleatoria = random.choice(alfabeto) + random.choice(alfabeto) + random.choice(alfabeto) + random.choice(numeros) +random.choice(alfabeto)  + random.choice(numeros)  + random.choice(numeros)
        check_placa = contemPlaca(placa_aleatoria)

    return placa_aleatoria


# Esta função cria um carro aleatório. O carro é um dicionario com
# placa, ano, marca e modelo. A placa deve ser gerada pela função
# placaAleatoria() que já foi implementada. A marca é uma escolha
# equiprovavel entre ["chevrolet","volkswagem",fiat"]. Se a marca
# for chevrolet, o carro é uma escolha equiprovável entre
# ["onix","cruze","camaro"]. Se a marca for "volkswagem", o modelo
# é uma escolha equiprovável entre ["polo","jetta","gol"]. Se
# a marca for fiat, o modelo é uma escolha equiprovável entre
# ["pulse","argo","moby"].
# Número estimado de linhas: 21
def carroAleatorio():
    # seu código vem aqui.
    placa = placaAleatoria()
    ano = random.randrange(2000,2023)
    marcas = ["chevrolet", "volkswagem", "fiat"]
    carros_chevrolet = ["onix", "cruze", "camaro"]
    carros_volkswagem = ["polo", "jetta", "gol"]
    carros_fiat = ["pulse","argo","moby"]
    marca = random.choice(marcas)
    if marca == "chevrolet":
        modelo = random.choice(carros_chevrolet)
    elif marca == "volkswagem":
        modelo = random.choice(carros_volkswagem)
    elif marca == "fiat":
        modelo = random.choice(carros_fiat)

    carro_aleatorio = {
        "placa": placa,
        "ano": ano,
        "marca": marca,
        "modelo": modelo
    }

    return carro_aleatorio


# Esta função deve inicialmente apagar o conteúdo do
# arquivo de dados. Após isso, deve ser gerado um conjunto
# de 200 carros aleatórios. Tais carros devem ser inseridos
# no arquivo de dados, por meio da função addCarro().
# Número estimado de linhas: 4
def populaDados():
    # seu código vem aqui.
    file = open(filename, "w")
    for i in range(200):
        addCarro(carroAleatorio())
    file.close()


# Veja um exemplo de execução.
# Inicialmente o programa chama a função populaDados()
# inserindo 200 carros aleatórios no arquivo de dados. Isso
# é feito fora da função geraEstatistica().
# Após isso, é chamada uma função manualAddCarro() ainda
# fora da função geraEstatistica().
# Suponha que o usuário digitou os dados abaixo
# Digite a placa:BBB1B22
# Digite ano:2000
# Digite marca:Honda
# Digite Modelo:Fit
# Agora foi finalmente chamada a função geraEstatistica().
# Primeiramente ela imprime uma lista de anos, e o número
# de carros por ano, conforme abaixo. Depois uma lista de marcas
# e o número de carros por marca. Finalmente uma lista de
# modelos, e o número de carros por modelo. Note que os valores
# podem diferir, pois a geração é aleatória. Note
# também que os anos/marcas/modelos são impressos em ordem crescente.
# Abaixo a saída da função geraEstatística.
# -- Numero de carros por ano ---
# ano 2000: 1 carro(s)
# ano 2015: 26 carro(s)
# ano 2016: 37 carro(s)
# ano 2017: 42 carro(s)
# ano 2018: 36 carro(s)
# ano 2019: 31 carro(s)
# ano 2020: 28 carro(s)
# -- Numero de carros por marca ---
# marca Honda: 1 carro(s)
# marca chevrolet: 64 carro(s)
# marca fiat: 75 carro(s)
# marca volkswagem: 61 carro(s)
# -- Numero de carros por modelo ---
# modelo Fit: 1 carro(s)
# modelo argo: 29 carro(s)
# modelo camaro: 19 carro(s)
# modelo cruze: 23 carro(s)
# modelo gol: 18 carro(s)
# modelo jetta: 25 carro(s)
# modelo moby: 20 carro(s)
# modelo onix: 22 carro(s)
# modelo polo: 18 carro(s)
# modelo pulse: 26 carro(s).
#
# Número de Linhas Esperado: 3+14, sendo 3 nesta função
# e 14 numa função auxiliar.
def geraEstatistica():
    # seu código vem aqui.
    carros = carregaCarros()
    df = pd.DataFrame(carros)
    
    print("-- Numero de carros por ano --")
    for i in range(2000, 2023):
        print(f"Ano {i}: " + str(df.loc[df["ano"] == i]["placa"].count()))
    
    print("-- Numero de carros por marca --")
    for i in ["chevrolet", "volkswagem", "fiat"]:
        print(f"Marca {i}: " + str(df.loc[df["marca"] == i]["placa"].count()))

    print("-- Numero de carros por modelo --")
    for i in ["onix", "cruze", "camaro", "polo", "jetta", "gol", "pulse","argo","moby"]:
        print(f"Modelo {i}: " + str(df.loc[df["modelo"] == i]["placa"].count()))


def manualAddCarro():
    placa = input("Digite a placa:")
    ano = int(input("Digite ano:"))
    marca = input("Digite marca:")
    modelo = input("Digite Modelo:")
    addCarro({"placa": placa, "ano": ano, "marca": marca, "modelo": modelo})


populaDados()
manualAddCarro()
geraEstatistica()
