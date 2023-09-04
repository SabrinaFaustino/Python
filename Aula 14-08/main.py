carros = ["Ford KA", "Volkswagen Fusca", "Chevrolet Celta", "Volkswagen Up Tsi", "Volkswagen Kombi"]
precos = [50, 60, 1000000, 200, 300]

def acha_maior(valores):
    indice_maior = 0 
    maior = valores[indice_maior]

    for i in range(len(valores)):
        if valores[i] > maior:
            maior = valores[i]
            indice_maior = i
    return indice_maior

lista = [2,45,6,77,8]
local_maior = acha_maior(lista)
print(acha_maior(precos))
#print(f"O carro mais caro é o {carros[indice_maior]} e vale R${precos[indice_maior]}")

matriz = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(f"O elemento matriz[{i}][{j}] = {matriz[i][j]}")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = 0
        print(f"O elemento matriz[{i}][{j}] = {matriz[i][j]}")

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i==j:
            print(matriz[i][j])

matriz = []

for i in range(3):
    linha = []
    for i in range(3):
        linha.append(i+1)
    matriz.append(linha)
    print(matriz)

