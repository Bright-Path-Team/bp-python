# Bibliotecas importadas
from utils.methods import *
from dotenv import load_dotenv
import os

# Inicializa o dotenv para utilizar as variáveis de ambiente
load_dotenv()
 # Altere conforme seu sistema operacional (Linux/Mac = clear | Windows = cls)
clear_cmd : str = "cls"

# Variáveis para armazenar um divisor que deixa o painel mais organizado para o usuário
logo : str = """██████╗ ██████╗ ██╗ ██████╗ ██╗  ██╗████████╗    ██████╗  █████╗ ████████╗██╗  ██╗
██╔══██╗██╔══██╗██║██╔════╝ ██║  ██║╚══██╔══╝    ██╔══██╗██╔══██╗╚══██╔══╝██║  ██║
██████╔╝██████╔╝██║██║  ███╗███████║   ██║       ██████╔╝███████║   ██║   ███████║
██╔══██╗██╔══██╗██║██║   ██║██╔══██║   ██║       ██╔═══╝ ██╔══██║   ██║   ██╔══██║
██████╔╝██║  ██║██║╚██████╔╝██║  ██║   ██║       ██║     ██║  ██║   ██║   ██║  ██║
╚═════╝ ╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
                                                                                """
divider : str = "\n" + "=" * 20 + "\n"

# Garante que ao inicializar o programa, o prompt de comando ficará limpo
os.system(clear_cmd)

# Quando o programa inicia pela primeira vez e o servidor está desligado, o painel CMD fica desligado por um bom tempo, então para a UX, o usuário deve saber que o programa está operando realizando verificações
return_message("Verificando a conexão com o servidor...")

# Variáveis de ambiente
ip_address : str = os.getenv("ip")

while True:
     # Imprime a logo da empresa e dois divisores, facilitando assim a visualização dos dados
    print(divider)
    bright_message(logo)
    print(divider)
    # Operador que checa o status da conexão com o servidor para dar um status ao usuário
    return_message(f"🔒 Conexão segura estabelecida com o serviço Cloud") if check_connection(ip_address) else error_message("⛔ Problema ao estabelecer conexão com o serviço cloud, o programa pode não funcionar corretamente!")
    print(divider)

    print("[1] - Monitoramento da placa leste")
    print("[2] - Monitoramento da placa oeste")
    print("[3] - Monitoramento da eficiência energética")
    print("[4] - Salvar os dados em um arquivo JSON")
    print("[5] - Gerar gráfico de monitoramento")
    print("[99] - Encerrar o programa")

    # Verifica se o número fornecido pelo usuário é do tipo inteiro
    try:
        opcao_usuario : int = int(input("Selecione uma opção: "))
    # Caso um valor não inteiro seja identificado, o programa gera uma exceção, retornando ao fluxo principal
    except ValueError:
        os.system(clear_cmd)
        error_message("Valor inválido, o programa aceita somente números!")
        continue # O continue faz com que o usuário retorne ao fluxo principal do programa

    match opcao_usuario:
        case 1:
            os.system(clear_cmd)
            print_info(ip_address, "east")
        case 2:
            os.system(clear_cmd)
            print_info(ip_address, "west")
        case 3:
            os.system(clear_cmd)
            print_info(ip_address, "efficiency")
        case 4:
            save_data(request_info(ip_address, "east"), request_info(ip_address, "west"), request_info(ip_address, "efficiency"))
        case 5:
            os.system(clear_cmd)
            plot_data()
        case 99:
            os.system(clear_cmd)
            bright_message(logo)
            return_message("Programa encerrado com suceso!")
            break
        case _:
            os.system(clear_cmd)
            error_message("Opção inexistente!")
            continue
