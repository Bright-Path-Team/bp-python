# Python - GS

## Descrição do projeto
Esse projeto foi desenvolvido inteiramente em python sem nenhum uso de Frameworks com o principal objetivo de criar um painel informativo com as informações do [IoT](https://github.com/Bright-Path-Team/bp-edge), de um sistema de paineis solares que verifica a eficiência energética de duas placas solares (uma a leste e a outra a oeste) e a média da eficiência energética de cada uma delas!

## Requisitos do sistema

### Requisitos Funcionais (RF)
1. Verificação de Conexão ao Servidor
1.1 O sistema deve verificar a conexão com o servidor no endereço IP configurado em um arquivo .env.
2. Interatividade com o Usuário via Menu
2.1 Deve apresentar um menu interativo com as seguintes opções:
3. Monitoramento da placa leste.
3.1 Monitoramento da placa oeste.
3.2 Monitoramento da eficiência energética.
3.3 Salvar dados coletados em um arquivo JSON.
3.4 Gerar gráficos de monitoramento.
3.5 Encerrar o programa.
4. Coleta de Dados de Monitoramento
4.1 O sistema deve realizar requisições a um servidor para obter os valores de:
4.1.1 Desempenho da placa solar leste.
4.1.2 Desempenho da placa solar oeste.
4.1.3 Eficiência energética média das placas.
5. Armazenamento de Dados
5.1 O sistema deve salvar os dados coletados em um arquivo JSON, com o formato adequado para posterior análise.
6. Geração de Gráficos
6.1 O sistema deve gerar gráficos dos dados coletados (placa leste, placa oeste e eficiência energética) em função do tempo.
7. Mecanismo de Reconexão
7.1 Caso a conexão com o servidor falhe, o sistema deve tentar reconectar automaticamente após um temporizador configurável.
8 Mensagens de Feedback
8.1 Deve exibir mensagens claras para o usuário indicando status, como sucesso na conexão, erros ou progresso das operações.
9. Encerramento do Programa
9.1 O programa deve permitir ao usuário finalizar a execução de forma segura, exibindo uma mensagem de encerramento.

### Requisitos Não Funcionais (RNF)
1. Interface de Linha de Comando (CLI)
1.1 O sistema deve operar em um ambiente de linha de comando, com mensagens formatadas para facilitar a leitura.
2. Configuração via Variáveis de Ambiente
2.1 O endereço IP do servidor deve ser configurado em um arquivo .env.
3. Desempenho
3.1 O tempo de resposta para verificar a conexão com o servidor deve ser adequado, com um timeout configurável.
3.2 Gráficos devem ser gerados em menos de 5 segundos para conjuntos de dados típicos.
4.Manutenção e Extensibilidade
4.1 O código deve ser modular, com funções reutilizáveis para operações como requisições, exibição de mensagens e manipulação de dados.
4.2 O sistema deve suportar expansão futura, como monitoramento de novas variáveis.
5. Compatibilidade
5.1 Deve ser compatível com sistemas operacionais Windows, Linux e Mac, com a possibilidade de configurar o comando de limpeza (cls ou clear).
6. Segurança
6.1 O sistema não utiliza nenhum tipo de conexão com outros servidores além do servidor que estão sendo feitas as requisições, isto é, não coleta nenhum dado do usuário.
7. Conformidade com Padrões
7.1 O JSON gerado deve seguir o padrão ISO para timestamps.
7.2 As mensagens devem usar códigos ANSI para realce de texto, garantindo a leitura em terminais compatíveis.
8. Dependências e Instalação
8.1 O sistema deve depender apenas de bibliotecas amplamente suportadas e de fácil instalação via pip (requests, dotenv, matplotlib).
