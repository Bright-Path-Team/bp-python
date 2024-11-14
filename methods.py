def alertMessage(message : str, spaces : str) -> None:
    """
    Função que utiliza o código Ansi para deixar o texto em vermelho

    Código ANSI é uma sequência de escape iniciada por '\ 033[' seguida por um código de cor, e terminada por m. Para resetar o estilo (voltar ao padrão), usa-se o código '\ 033[0m'
    """
    print(f"\033[31m {spaces}{message}\n \033[0m")

def copyValues(ip : str) -> list:
    """
    Função para realizar a leitura dos valores do STH Comet e gerar uma lista para que os valores possam ser armazenados e se necessários manipulados

    :return: List
    """
    valueList : list = [1,2,3]
    return valueList


def checkEfficiency(values : list) -> int:
    """
    Função para checar a eficiência da coleta de energia dos paineis solares

    :return: int
    """
    number : int = 1
    return number

def userGuide() -> str:
    return "Olá usuário! Seja bem-vindo(a) ao programa da Bright Path. Somos uma empresa dedicada ao avanço em tecnologias sustentáveis!\nNosso projeto foi desenvolvido para conscientização da população sobre como utilizar a energia elética de maneira sustentável."
