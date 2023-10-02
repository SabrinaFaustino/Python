import pandas as pd
dados = pd.read_csv("C:\\Users\\logonrmlocal\\Downloads\\Teste\\dado_mg.csv")

dic = {}
for key,value in zip(dados.columns[0].split(";"),dados.values[0][0].split(";")):
    dic[key] = [value]
print(dic)

j=0
for key in dic.keys():
    for i in range(len(dados)):
        dic[key].append(dados.values[i][0].split(";")[j])
    j+=1
print(dados.values[1][0])
print(dic)

