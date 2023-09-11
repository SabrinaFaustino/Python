def forcar_opcao(msg, lista_opcoes):
    resposta= input(msg)
    while resposta not in lista_opcoes:
        print("Digite uma resposta cadastrada! ")
        resposta = input(msg)
    return resposta

def printar_dicionario(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            printar_dicionario(dic[key])
        else:
            print(f"{key} : {dic[key]}")
    return

vinhos = {
    'Tipo' : ['Tinto', 'Rosé', 'Seco', 'Branco', 'Suave'],
    'Teor alcoólico' : [11,15,12,13,10],
    'Safra' : [1958,1962,1970,1994,2002],
    'Preço' : [100,130,20,25,50],
    'Nacionalidade' : ['Chileno', 'Argentino', 'Françês', 'Italiano', 'Jundiaiense']
}

lista_vinhos = [str(i) for i in range(len(vinhos['Tipo']))]
'''
lista_vinhos = []
for i in range(len(vinhos['Tipo'])):
    lista_vinhos.append(str(i))
'''

compra = {"Endereço" : {
            'Rua' : '',
            'Bairro' : '',
            'Cidade' : '',
            'Numero' : '',
            'CEP' : '',
            'Estado' : '',
        },
          "Valor Total" : 0,
          "Vinhos" : {}}

papel = forcar_opcao("Você é cliente ou funcionário? (c/f) ", ['c','f'])
print(".\n"*5)
if papel == 'c':
    print("Seja bem vindo!!! ")
    print('='*30)
    for key in compra['Endereço'].keys():
        info = input(f"Diga seu/a {key}: ")
        compra['Endereço'][key] = info

    while True: 
        print("Essas são as opções da vinhos: ")
        for i in range(len(vinhos['Tipo'])):
            print(f"{i} - {vinhos['Tipo'][i]}")
        opcao = int(forcar_opcao("Qual vinho lhe interessou mais? ", lista_vinhos))
        for key in vinhos.keys():
            print(f"{key} : {vinhos[key][opcao]}")
        comprar = forcar_opcao("Vai levar? (s/n) ", ['s','n'])
        if comprar == 's':
            compra['Valor Total'] += vinhos['Preço'][opcao]
            nome = vinhos['Tipo'][opcao]
            if nome not in compra['Vinhos'].keys():
                compra['Vinhos'][nome] = 1
            else:
                compra['Vinhos'][nome] +=1
        continuar = forcar_opcao("Você gostaria de ver mais vinhos? (s/n) ", ['s','n'])
        if continuar == 's':
            continue
        else:
            print("Obrigada pela compra: ")
            printar_dicionario(compra)
            break
else:
    acoes = ['Alterar preço', 'Remover', 'Cadastrar']
    print("Essas são as opções de ação: ")
    for i in range(len(acoes)):
        print(f"{i} - {acoes[i]}")
    opcao = forcar_opcao("O que deseja fazer? ", ['0','1','2'])
    if opcao == '0':
        for i in range(vinhos['Tipo']):
            print(f'{i}- {vinhos["Tipo"][i]}')
        alterar = forcar_opcao("Qual vinho será alterado? ", lista_vinhos)
        novo_valor = float(input("Diga o novo valor: "))
        vinhos['Preço'][alterar] = novo_valor
    elif opcao == '1':
        for i in range(len(vinhos['Tipo'])):
            print(f'{i}- {vinhos["Tipo"][i]}')
        remover = int(forcar_opcao("Qual vinho será removido? ", lista_vinhos))
        for key in vinhos.keys():
            vinhos[key].pop(remover)
    else:
        for key in vinhos.keys():
            cadastrar = input(f"Digite o {key} do vinho: ")
            vinhos[key].append(cadastrar)
        print("Vinho cadastrado com sucesso!")
        printar_dicionario(vinhos)
