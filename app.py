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
from utils.methods import *
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

# Garante que ao inicializar o programa, o prompt de comando ficará limpo
print(spaces)

# Variáveis de ambiente
ip_address : str = os.getenv("ip")
masked_ip_address : str = mask_ip(ip_address)

while True:
    # Imprime a logo da empresa e um divisor, facilitando assim a visualização dos dados
    print(logo)
    print(divider)
    print(f"🔒 Conexão segura estabelecida com o serviço Cloud")
    print(divider)
    print("[1] - Monitoramento da placa leste")
    print("[2] - Monitoramento da placa oeste")
    print("[3] - Gerar gráfico de eficiência")
    print("[99] - Encerrar o programa")
    # Verifica se o número fornecido pelo usuário é do tipo inteiro
    try:
        opcao_usuario = int(input("Selecione uma opção > "))
    # Caso um valor não inteiro seja identificado, o programa gera uma exceção, retornando ao fluxo principal
    except ValueError:
        error_message("Valor inválido, o programa aceita somente números!", spaces)
        continue # O continue faz com que o usuário retorne ao fluxo principal do programa

    match opcao_usuario:
        case 1:
            print(spaces)
            pass
        case 99:
            print(spaces)
            print(logo)
            returnMessage("Programa encerrado com suceso!", spaces)
            break
        case _:
            error_message("Opção inexistente!", spaces)
            continue
