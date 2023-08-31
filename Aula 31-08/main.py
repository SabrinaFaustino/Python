jogo = {"São Paulo" : "Vencedor", "Corinthias" : "Perdedor"}
#print(jogo["Corinthias"])
jogo["Palmeiras"] = "Sem Mundial"
#print(jogo) 
jogo["São Paulo"] = [jogo["São Paulo"]]
#print(jogo)
#print(type(jogo["São Paulo"]))
jogo["São Paulo"].append("Tricolor")
#print(jogo)

vinhos = {
        "Tipo" : ["Tinto","Seco","Doce","Suave","Branco"], 
        "Preço" : [50,100,90,70,65],
        "Safra" : [1927,1935,1910,1951,1941],
        "Teor Alcoólico" : [10,15,13,11,16]
        }

#de a um usuario todos os tipos de vinhos da casa
#permita que o usuario escolha a respeito de qual vinho ele quer informações
#printe na tela todas as informações sobre o vinho escolhido

def forcar_opcao(msg, lista_opcoes):
    resposta = input(msg)
    while not resposta in lista_opcoes:
        resposta = input(msg)
    return resposta

print("Seja bem-vindo(a) a vinheria!!!")
valor_total = 0
compra = {}
while True: 
    s_ou_n = forcar_opcao("Você gostaria de conhecer nossos vinho? (s/n)", ["s","n"])
    if s_ou_n == "s":

        if not compra:
            endereco = input("Diga o endereço de entrega: ")
            compra["endereco"] = endereco
            compra["gasto_total"] = 0
            compra["vinhos_comprados"] = []

        i=0
        for tipo in vinhos["Tipo"]:
            print(f"{i} - {tipo}")
            i+=1

        opcao = int(forcar_opcao("Digite a opção desejada: ", ["0","1","2","3","4"]))

        for key in vinhos.keys():
            print(f"{key} : {vinhos[key][opcao]}")

        escolha = forcar_opcao("Deseja comprar o vinho escolhido? (s/n)", ["s","n"])
        if escolha == "s":
            compra["gasto_total"]+=vinhos["Preço"][opcao]
            compra["vinhos_comprados"].append(vinhos["Tipo"][opcao])
            print(f"Você comprou o vinho {vinhos['Tipo'][opcao]}")
            print(f"Seu carrinho está em R${compra['gasto_total']}")
        else:
            print("Tchau")
            break
    else:
        print(f"Resumo do seu pedido: R${valor_total}")
        for key in compra.keys():
            print(f"{key} : {compra[key]}")
        print("Volte sempre")
        break
print(compra)