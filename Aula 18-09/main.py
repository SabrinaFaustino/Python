import requests
import pandas as pd


url = "https://viacep.com.br/ws/08550010/json/"
response = requests.get(url)
response = response.json()

#pergunte ao usuário se ele é cliente ou funcionário
#se for cliente, de as opções de vinhos da casa e pergunte seu endereço
#pergunte informações a respeito de qual ele quer ver
#pergunte se ele vai comprar o vinho escolhido no item anterior
#caso queira, adicione ao carrinho dele o vinho e seu preço

def verifica_endereco():
    while True: 
        cep = input("Diga seu cep: ")
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        if response.status_code == 200:
            print("Essas são as informações a respeito do seu cep: ")
            response = response.json()
            for key in response.keys():
                print(f"{key} : {response[key]}")
            correto = forca_opcao("Estão corretas? (s/n) ", ["s","n"])
            if correto == "s":
                numero = input("Diga o numero da residência: ")
                response['numero'] = numero
                return response
            else:
                print("Cep inválido")

def forca_opcao(msg,lista_opcoes):
    resposta = input(msg)
    while resposta not in lista_opcoes:
        print("Digite uma resposta cadastrada! ")
        resposta = input(msg)
    return resposta

def printa_dicionario(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            printa_dicionario(dic[key])
        else:
            print(f"{key} : {dic[key]}")
    return

def login():
    usuario = "admin"
    senha = "4321"
    user = input("Digite o seu usuario: ")
    password = input("Digite sua senha: ")
    tentativas = 1
    while not (user == usuario and password == senha) and tentativas < 3:
        print(f"Usuário ou senha incorretos. Você tem mais {3-tentativas} tentativas")
        user = input("Digite o seu usuario: ")
        password = input("Digite sua senha: ")
        tentativas +=1
    if user == usuario and password == senha:
        return True
    return False
        

def alterar():
    for i in range(len(vinhos['tipo'])):
        print(f"{i} - {vinhos['tipo'][i]}")
    alterar = int(forca_opcao("Qual vinho será alterado ? ",lista_vinhos))
    novo_valor = int(input("Diga o novo valor : "))
    vinhos['tipo'][alterar] = novo_valor
    return

def cadastrar():
    for key in vinhos.keys():
        info = input(f"Diga o/a novo/a {key} : ")
        vinhos[key].append(info)
    print(pd.DataFrame(vinhos))
    return

def remover():
    for i in range(len(vinhos['tipo'])):
        print(f"{i} - {vinhos['tipo'][i]}")
    removido = int(forca_opcao("Qual vinho será removido ? ",lista_vinhos))
    for key in vinhos.keys():
        vinhos[key].pop(removido)
    print(pd.DataFrame(vinhos))
    return

vinhos = {
    'tipo' : ['tinto', 'rosé', 'seco', 'branco', 'suave'],
    '% alcoólico' : [11,15,12,13,10],
    'safra' : [1958,1962,1970,1994,2002],
    'preço' : [100,130,20,25,50],
    'Nacionalidade' : ['chileno','argentino','françês','italiano','jundiaiense'],
    'Estoque' : [1,3,0,2,1]
}

import pandas as pd
print(pd.DataFrame(vinhos))
lista_vinhos = [str(i) for i in range(len(vinhos['tipo']))]
'''
lista_vinhos = []
for i in range(len(vinhos['tipo'])):
    lista_vinhos.append(str(i))
'''
compra = {
    'endereco' : {},
    'valor total' : 0,
    'vinhos' : {}
}

papel = forca_opcao("Você é cliente ou funcionário ? (c/f) ",['c','f'])
if papel == 'c':
    print("Seja bem vindo!!! ")
    compra['endereco'] = verifica_endereco()
    while True:
        print('Essas são as nossas opções de vinhos :')

        for i in range(len(vinhos['tipo'])):
            print(f"{i} - {vinhos['tipo'][i]}")
        opcao = int(forca_opcao("Qual vinho lhe interessou mais ? ",lista_vinhos))

        for key in vinhos.keys():
            print(f"{key} : {vinhos[key][opcao]}")
        comprar = forca_opcao("Vai levar ? (s/n) ",['s','n'])

        if comprar == 's':
            nome = vinhos['tipo'][opcao]
            if vinhos['Estoque'][opcao] == 0:
                print("Infelizmente não temos esse vinho no estoque!")
                continue
            else:
                vinhos['Estoque'][opcao] -= 1

            compra['valor total'] += vinhos['preço'][opcao]
            
            
            if nome not in compra['vinhos'].keys():
                compra['vinhos'][nome] = 1
            else:
                compra['vinhos'][nome] += 1

        continuar = forca_opcao("Voce gostaria de ver mais vinhos ? (s/n)",['s','n'])

        if continuar == 's':
            continue
        else:
            print("Obrigado pela compra : ")
            printa_dicionario(compra)
            break
else:
    if login():
        while True:
            acoes = ['alterar preço','remover','cadastrar','sair']
            print("Essas são as opções de ação: ")
            for i in range(len(acoes)):
                print(f"{i} - {acoes[i]}")
            opcao = forca_opcao('O que vc deseja fazer ? ',['0','1','2','3'])
            if opcao == '0':
                alterar()
            elif opcao == '2':
                cadastrar()
            elif opcao == '1':
                remover()
            else:
                break