vinhos = {
    'Tipo' : ['Tinto', 'Rosé', 'Seco', 'Branco', 'Suave'],
    '% alcoólico' : [11,15,12,13,10],
    'Safra' : [1958,1962,1970,1994,2002],
    'Preço' : [100,130,20,25,50],
    'Nacionalidade' : ['Chileno', 'Argentino', 'Françês', 'Italiano', 'Jundiaiense']
}

def forcar_opcao(msg, lista_opcoes):
    resposta = input(msg)
    while not resposta in lista_opcoes:
        resposta = input(msg)
    return resposta

print("Bem-vindo(a) á nossa Vinheria")
print('=' * 30)

valor_total = 0
carrinho = {}
cliente_func = forcar_opcao("Você é funcionário ou cliente? (f/c)", ['f','c'])
endereco = input("Digite o seu endereço: ")
if cliente_func == 'c':
    while True:
        i=0
        for tipo in vinhos["Tipo"]:
            print(f"{i} - {tipo}")
            i+=1
        
        if not carrinho:
            carrinho["endereco"] = endereco
            carrinho["valor_total"] = 0
            carrinho["vinhos_escolhidos"] = []
            carrinho["quantidade"] = []

        escolha = int(forcar_opcao("Qual vinho você gostaria de ver as informações: ", ["0","1","2","3","4"]))
        for key in vinhos.keys():
            print(f"{key} : {vinhos[key][escolha]}")

        comprar = forcar_opcao("Gostaria de comprar o vinho escolhido? (s/n)", ['s','n'])
        if comprar == 's':
            qtd = input(f"Quantos vinhos você gostaria do {vinhos['Tipo'][escolha]}: ")
            valor_total = int(qtd) * vinhos['Preço'][escolha]
            carrinho["valor_total"]+=valor_total
            carrinho["vinhos_escolhidos"].append(vinhos['Tipo'][escolha])
            carrinho['quantidade'].append(qtd)
            print(f"Foi adicionado R$ {valor_total} no seu carrinho")
        else:
            print("Os vinhos no carrinho são:")

            for i in range(len(carrinho['vinhos_escolhidos'])):
                print(f"{i} - {carrinho['vinhos_escolhidos'][i]} - {carrinho['quantidade'][i]}x")
                
            print(f"\nO valor total é de R$ {carrinho['valor_total']}")
            print(f"O endereço de entrega vai ser na {carrinho['endereco']}\n")
            break

        
        


