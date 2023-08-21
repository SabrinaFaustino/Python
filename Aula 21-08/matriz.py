import random

def cria_matriz(linhas,colunas):
    matriz = []
    for l in range(linhas):
        matriz.append([])
        for c in range(colunas):
            num = random.randint(0,10)
            matriz[l].append(num)
    return matriz

def mostra_matriz(matriz):
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            print(f"[{matriz[l][c]:^5}]", end="")
        print()

def soma_elementos(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma += vetor[i]
    return soma

alunos = 10
notas = cria_matriz(5,alunos)
mostra_matriz(notas)
pesos = [1,2,3,2,1]
medias = []

for j in range(alunos):
    soma = 0
    soma_pesos = soma_elementos(pesos)
    for i in range(len(pesos)):
        soma+=pesos[i]*notas[i][j]
    media = soma/soma_pesos
    medias.append(round(media,1))
print(medias)

