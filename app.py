"""
Requisitos do Sistema: 

1. Implementar um menu de opções com as principais funcionalidades oferecidas pelo sistema. 
2. Realizar validações nas entradas de dados do usuário. 
3. Aplicar adequadamente o tratamento de exceções. 
4. Utilizar estruturas de decisão e repetição. 
5. Utilizar funções com passagem de parâmetros e retorno. 
6. Utilizar listas e dicionários para armazenar dados. 
7. Utilizar arquivos JSON como para persistência de dados. 
"""
# Bibliotecas importadas
from methods import *
from dotenv import load_dotenv
import os

# Inicializa o dotenv para utilizar as variáveis de ambiente
load_dotenv()

# Variáveis para armazenar um divisor que deixa o painel mais organizado para o usuário
logo : str = """██████╗ ██████╗ ██╗ ██████╗ ██╗  ██╗████████╗    ██████╗  █████╗ ████████╗██╗  ██╗
██╔══██╗██╔══██╗██║██╔════╝ ██║  ██║╚══██╔══╝    ██╔══██╗██╔══██╗╚══██╔══╝██║  ██║
██████╔╝██████╔╝██║██║  ███╗███████║   ██║       ██████╔╝███████║   ██║   ███████║
██╔══██╗██╔══██╗██║██║   ██║██╔══██║   ██║       ██╔═══╝ ██╔══██║   ██║   ██╔══██║
██████╔╝██║  ██║██║╚██████╔╝██║  ██║   ██║       ██║     ██║  ██║   ██║   ██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
                                                                                """
divider : str = "\n" + "=" * 20 + "\n"
spaces : str = "\n" * 130

# Garante que ao inicializar o programa, o CMD ficará limpo
print(spaces)

# Variáveis de ambiente
ip_address : str = os.getenv("ip")

while True:
    print(logo)
    print(divider)
    print("[1] - Opção 1")
    print("[99] - Encerrar o programa")
    # Verifica se o número fornecido pelo usuário é do tipo inteiro
    try:
        opcao_usuario = int(input("Selecione uma opção > "))
    # Caso um valor não inteiro seja identificado, o programa gera uma exceção, retornando ao fluxo principal
    except:
        print("Valor inválido!")

    match opcao_usuario:
        case 1:
            pass
        case 99:
            print("Encerrando o programa...")
            break
        case _:
            print(spaces)
            print("Opção inválida!")
