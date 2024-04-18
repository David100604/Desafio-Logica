import string


def maior_letra(texto):
    texto = texto.lower()
    validar_texto(texto)
    return max(texto)


def validar_texto(texto):
    return texto.isalnum()

def get_quantidade(): 
    quantidade_vezes = int(input("Insira a quantidade de vezes que você deseja executar o código: "))
    return quantidade_vezes


quantidade_vezes = get_quantidade()
for i in range(quantidade_vezes):
    texto = input(f"Entrada {i + 1}: ")
    print(f"Saída {i + 1}: " + maior_letra(texto))