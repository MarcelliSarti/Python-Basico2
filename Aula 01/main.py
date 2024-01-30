# introdução à python

# python não usa ponto e vírgula nem chaves.
# A identação é feita com tabulação.

print("Hello")
x = 1
if x == 1:
    print("x vale 1")

# string in python
nome = "Jorge"
idade = "35"
print("Havia um homem chamado " + nome + " com " + idade + " anos")

# As variáveis não são fortemente tipadas em python
# Exemplo de string
x = "5"
#  X passa agora a ser int.
x = 5
# X passa a ser float
x = 5.5
# X passa a ser boolean
x = True

# Algumas operações sobre strings:
frase = "Olá mundo mundo vasto mundo."
print(frase)
print(frase.lower())
print(frase.upper())
# As operacoes acima não mudam o conteudo de frase.
# Para mudar o conteúdo é preciso fazer o seguinte:
frase = frase.upper()
print("Nova frase2:" + frase)
print("isupper:" + str(frase.isupper()))
print("islower:" + str(frase.islower()))

# posso acessar letras de uma string:
print(frase[0] + frase[1] + frase[2])

# Posso buscar a primeira ocorrencia de uma substring
print(frase)
print("Primeira ocorrencia de MUNDO:" + str(frase.index("MUNDO")))

# Posso substituir uma string por outra
frase = frase.replace("MUNDO", "Planeta")
print(frase)

# Numeros em python
x = 5
# Para imprimir é necessário usar o str
print("Numero " + str(5))
print("2^10=" + str(pow(2, 10)))
print("raiz(2)=" + str(pow(2, 0.5)))

print("MAX=" + str(max(1, 10, 2, 3, 4)))
print("MIN=" + str(min(1, 10, 2, 3, 4)))
# arredondamento
print("ROUND 3.7 = " + str(round(3.7)))
print("ROUND 3.2 = " + str(round(3.2)))
# chão e teto
from math import *

print("chao 3.7 = " + str(floor(3.7)))
print("teto 3.7 = " + str(ceil(3.7)))
# raiz
print("raiz(2)=" + str(sqrt(2)))

print("LENDO DADOS DO USUÁRIO")

# nome = input("Entre seu nome:")
# idade = input("Entre sua idade:")
# print("Ola " + nome + "!")
# print("idade " + idade + "!")
#
# num1 = input("Entre um número:")
# num2 = input("Entre um número:")
# result = num1+num2
# print(result)
# result = float(num1)+float(num2)
# print(result)
# result = int(num1)+int(num2)
# print(result)

print("LISTAS EM PYTHON")
amigos = ["Paulo", 2, True]
amigos = ["Paulo", "Andre", "Joao", "Luis", "Marcos"]

print(amigos)
print("Primeiro elemento:")
print(amigos[0])
print("Último elemento:")
print(amigos[-1])
print("Penúltimo elemento:")
print(amigos[-2])
print("Posição 2 até o final")
print(amigos[2:])
print("Posição 2 (incluso) até 4(não incluso)")
print(amigos[2:4])

# Uso do pop
x = amigos.pop()
print("x=" + x)
print("Amigos=" + str(amigos))

# Uso do append
amigos.append("Mateus")
print("Amigos=" + str(amigos))
print("index(Mateus)=" + str(amigos.index("Mateus")))

# Uso do count
amigos.append("Mateus")
amigos.append("Mateus")
print("Amigos=" + str(amigos))
print("count(Mateus)=" + str(amigos.count("Mateus")))

# Uso do sort
amigos.sort()
print(amigos)

# uso do reverse
amigos.reverse()
print(amigos)

# Copiar versus não copiar:
print("------");
novo = amigos
# sem copy, pop retira de ambos.
novo.pop()
print(novo)
print(amigos)

# com copy, retira só da cópia.
novo = amigos.copy()
novo.pop()
print(novo)
print(amigos)

# tuplas em python. São imutáveis
coordenada = (2, 3)
print(coordenada[0])
# proibido o comando abaixo:
# coordenada[0]=3

coordenadas = [(3, 1), (2, 9), (3, 9), (3, 5)]
print(coordenadas)
# ordena pelo primeiro item da tupla. Em caso
# de empate, usa o segundo termo da tupla.
coordenadas.sort()
print(coordenadas)


# funções em python
def diga_ola():
    print("Ola Mundo")


print("Antes")
diga_ola()
print("Depois")

def cubo(n):
    return n * n * n

print(cubo(3))

# condicionais
eh_masculino = True
if eh_masculino:
    print("masc")
else:
    print("não masc")
eh_alto = False

if eh_masculino and eh_alto:
    print("masc and alto")
elif eh_masculino and not eh_alto:
    print("masc and not alto")
elif not eh_masculino and eh_alto:
    print("not masc and alto")
else:
    print("not masc not alto")

nome = input("Entre com seu nome:")
print("Nome:"+nome)

pi = float(input("Digite Pi:"))
print("Pi:"+str(pi))