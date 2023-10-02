'''lista = ['a','b','c']

while True:
    try:
        i = int(input("Digite um número: "))
        print(lista[i])

    except ValueError:
        print("Deve ser um inteiro")
    except IndexError:
        print(f"Deve ser um número entre 0 e {len(lista)-1}")
    except Exception as e:
        print(e)
    else:
        print("Operação realizada com sucesso")
        break
    finally:
        print("N sirvo p mta coisa")
'''
lista = ["Danilo","Calleri","Lucas Moura","Luciano"]

def valida_lista(lista):
    try:
        if type(lista) is not list:
            raise TypeError()
    except TypeError:
        print(f"Esse parâmetro {lista} deveria ser uma lista")
        return False
    else: 
        return True

def adiciona_nome(qtd,lista):
    if valida_lista(lista):
        for i in range(qtd):
            nome = input(f"Diga o {i+1}º nome: ")
            lista.append(nome)

    return lista
    
lista_nomes = adiciona_nome(2,"agfgdd")