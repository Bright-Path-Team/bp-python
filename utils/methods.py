import requests

def check_info(ip : str, param : str) -> str:
    """
    Essa função deve requisitar ao servidor informações de acordo com o que for solicitado pelo usuario
    """
    url = f"http://{ip}:1026/v2/entities/urn:ngsi-ld:Iot:001/attrs/{param}"

    payload = ""
    headers = {
    'fiware-service': 'smart',
    'fiware-servicepath': '/',
    'accept': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response

def error_message(message : str, spaces : str) -> None:
    """
    Função que utiliza o código Ansi para deixar o texto em vermelho

    Código ANSI é uma sequência de escape iniciada por '\ 033[' seguida por um código de cor, e terminada por m. Para resetar o estilo (voltar ao padrão), usa-se o código '\ 033[0m'
    """
    print(f"\033[31m {spaces}{message}\n \033[0m")


def returnMessage(message : str, spaces : str) -> None:
    """
    Função que utiliza o código Ansi para deixar o texto em vermelho

    Código ANSI é uma sequência de escape iniciada por '\ 033[' seguida por um código de cor, e terminada por m. Para resetar o estilo (voltar ao padrão), usa-se o código '\ 033[0m'
    """
    print(f"\033[32m {spaces}{message}\n \033[0m")


def mask_ip(ip : str) -> str:
    # Divide o IP em partes usando "."
    partes = ip.split('.')
    
    # Soma os dígitos de cada parte e aplica a fórmula
    partes_criptografadas = []
    for parte in partes:
        soma_digitos = sum(int(digito) for digito in parte)  # Soma dos dígitos
        valor_criptografado = soma_digitos * (9 / 3)  # Multiplicação por 3
        partes_criptografadas.append(str(int(valor_criptografado)))  # Converte para string
    
    # Junta as partes criptografadas em um "IP"
    ip_criptografado = '.'.join(partes_criptografadas)
    return ip_criptografado


def copy_values(ip : str) -> list:
    """
    Função para realizar a leitura dos valores do STH Comet e gerar uma lista para que os valores possam ser armazenados e se necessários manipulados

    :return: List
    """
    valueList : list = [1,2,3]
    return valueList


def check_efficiency(values : list) -> int:
    """
    Função para checar a eficiência da coleta de energia dos paineis solares

    :return: int
    """
    number : int = 1
    return number


def user_guide() -> str:
    return "Olá usuário! Seja bem-vindo(a) ao programa da Bright Path. Somos uma empresa dedicada ao avanço em tecnologias sustentáveis!\nNosso projeto foi desenvolvido para conscientização da população sobre como utilizar a energia elética de maneira sustentável."
