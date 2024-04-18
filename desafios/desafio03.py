

def get_nome():
    nome = input("\nNome: ")
    return nome

def get_quantidade(): 
    quantidade_vezes = int(input("Insira a quantidade de vezes que você deseja executar o código: "))
    return quantidade_vezes


def pegar_ultimo_sobrenome(nome):
    palavras = nome.split()
    ultimo_sobrenome = palavras.pop().upper()
    return ultimo_sobrenome

def separar_iniciais(nome):
    palavras = nome.split()
    palavras.pop()
    iniciais = []
    for palavra in palavras:
        iniciais.append(palavra[0].upper())
    return iniciais


def formatar_nome():
    quantidade_vezes = get_quantidade()
    saidas = []
    for i in range(quantidade_vezes):
        nome = get_nome()
        ultimo_sobrenome = pegar_ultimo_sobrenome(nome)
        iniciais = ". ".join(separar_iniciais(nome))
        saidas.append(f"Saida {i + 1}: {ultimo_sobrenome}, {iniciais}")

    print("\n")
    for saida in saidas:
        print(saida)    


formatar_nome()
    
