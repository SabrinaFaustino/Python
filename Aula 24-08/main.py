jogo = {"São Paulo":"Vencedor","Corinthias":"Perdedor"}
jogo["Corinthias"] = "Eliminado"
numeros = {"Pares" : [], "Ímpares": []}

for i in range(10):
    if i%2==0:
        numeros["Pares"].append(i)
    else:
        numeros["Ímpares"].append(i)
print(numeros)

def acha_maior(lista):
    indice_maior = 0
    maior = lista[0]
    for i in range (len(lista)):
        if lista[i]>maior:
            maior = lista[i]
            indice_maior = i
    return indice_maior    

carros = {"Modelos": ["UP","KA","Celta","Gol"],"Preço":[300,150,470,100]}
carros["Potência"] = [900,100,275,360]

local_mais_caro = acha_maior(carros["Preço"])
print(f"O carro mais carro é o {carros['Modelos'][local_mais_caro]} e vale R${carros['Preço'][local_mais_caro]},00")

local_mais_potente = acha_maior(carros["Potência"])
print(f"O carro mais potente é o {carros['Modelos'][local_mais_potente]} sua potência é de {carros['Potência'][local_mais_potente]}")

print("As informações pedidas são: ")
for key in carros.keys():
    print(f"{key} : {carros[key][local_mais_potente]}")

def garantir_resposta(lista_respostas,msg):
    resposta = input(msg)
    while not resposta in lista_respostas:
        resposta = input(msg)
    return resposta

import pandas as pd

while True:
    pergunta = garantir_resposta(["s","n"], "Deseja cadastrar um carro? ")

    if pergunta == "s":
        print("Diga as informações: ")
        for key in carros.keys():
            info = input(f"{key} : ")
            carros[key].append(info)
    else:
        print("Cadastro finalizado")
        print(pd.DataFrame(carros))
        break