def calcular_media():
    quantidade_alunos = get_quantidade() # chama a função para saber quantas vezes rodar
    saidas = [] # lista criada para armazenar as saídas
    for i in range(quantidade_alunos): # diz para o código seguinte rodar de acordo com função get_quantidade
        print(f"\nEntrada {i + 1}: ") # exibe a numeração da entrada
        nome = input("Escreva seu nome: ") # coleta o nome como string

        notas = [] # lista criada para armazenar as notas
        for i in range(4): # diz para o código rodar 4 vezes
            notas.append(int(input(f"Digite a {i + 1}º nota: "))) # coleta a nota inserida pelo usuário, transforma em int e adiciona na lista "notas"


        soma = sum(notas) # soma todos os valores dentro da lista "notas"
        media = soma / 4 # calcula a média

        saidas.append(f"Aluno = {nome} // Média = {media}") # adiciona a string com os resultados à lista "saidas"
        

    exibir_saidas(saidas) # chama a função para exibir as saídas passando a lista como parâmetro


''' Coleta a quantidade de vezes que o programa 
    irá rodar o cálculo de média de acordo com a 
    quantidade de alunos.'''
def get_quantidade(): 
    quantidade_alunos = int(input("Insira a quantidade de alunos que você deseja realizar a média: "))
    return quantidade_alunos



# Exibe cada um dos resultados        

def exibir_saidas(saidas):
    print("\n")
    for i, saida in enumerate(saidas):
        print(f"Saida {i + 1}: {saida}")

calcular_media() # executa a função "calcular_media"