dic = {"São Paulo" : "Vencedor", "Corinthias" : "Perdedor", "Palmeiras" : "Sem mundial", "Santos" : "Velho"}
time = input("Que time você torce? ")
print(f"Você é um {dic[time]}")

dic = {"chave1" : "valor1"}
#print(dic)
#print(dic["chave1"])
dic["chave2"] = "valor2"
dic["chave1"] = "novo valor"
#print(dic)
for key in dic.keys():
    print(dic[key])

dicionario = {}
dicionario["Pares"] = []
dicionario["Impares"] = []

for i in range(0,10):
    if i % 2 == 0:
        dicionario["Pares"].append(i)
    else:
        dicionario["Impares"].append(i)
print(dicionario)

for key in dicionario.keys():
    print(dicionario[key])

dicionario = {}
dicionario["Carros"] = ["Mini Cooper S Turbo", "Honda Civic SI 2.4", "Jeep Compass Turbo Diesel", "Subaru Imprenza WRX STI", "Nissan 370z Nismo", "Porsche Carrera GT"]
dicionario["Preços"] = [96_000, 125_500, 150_200, 259_900, 305_000, 900_000]
dicionario["Potência"] = []

for carro in dicionario["Carros"]:
    potencia = input(f"Digite a potência do {carro}: ")
    dicionario["Potência"].append(potencia)

import pandas as pd
dicionario = pd.DataFrame(dicionario)
print(dicionario)

def mais_caro(precos):
    maior = 0
    indice_maior = 0
    for i in range(len(precos)):
        if maior > 0:
            maior = precos[i]
            indice_maior = i
        elif maior > precos[i]:
            maior = precos[i]



