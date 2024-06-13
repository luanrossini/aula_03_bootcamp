import re
### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

quantidade = 10
preco = 2

if quantidade > 0 and preco > 0:
    print("Valor validos!")
else: 
    print("Valores invalidos!")

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

temperatura = 35

if temperatura < 0:
    print("Baixa")
if temperatura > 60:
    print("Alta")
else:
    print("Normal")

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

def filtrar_mensagem_de_erro(log):
    # Verifica se o nível de severidade do log é 'ERROR'
    if log['level'] == 'ERROR':
        # Imprime a mensagem do log
        print(log['message'])

# Exemplo de uso
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
filtrar_mensagem_de_erro(log)

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

usuario_teste = {'idade':25, 'email': 'teste@example.com'}


def validar_dados_usuario(usuario):
    idade = usuario.get('idade')
    email = usuario.get('email')

    # Verifica se a idade está no intervalo permitido
    if idade is None or not (18 <= idade <= 65):
        print("Erro: Idade inválida")
        return

    # Verifica se o email é válido usando uma expressão regular
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if email is None or not re.match(email_regex, email):
        print("Erro: Email inválido")
        return  
    print("Dados de usuário válidos")

validar_dados_usuario(usuario_teste)

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

transacao_teste = {'valor': 12000, 'hora': 20}

def validar_transacao(transacao):
    valor = transacao.get('valor')
    hora = transacao.get('hora')

        # Verifica se o valor e o horário são válidos
    if valor >= 10000 and not (9 <= hora <= 18):
        print("ATENÇÃO: Hora e valor da transação fora dos parâmetros")
        return

    # Verifica se o valor está acima do parâmetro permitido
    if valor is None or valor >= 10000:
        print("ATENCAO: Valor acima do parâmetro")
        return

    # Verifica se o horário é válido
    if hora is None or not (9 <= hora <= 18):
        print("ATENCAO: Horario da transacao fora do parâmetro")
        return 
    print("Dados de transação válidos")

validar_transacao(transacao_teste)


### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = "Exemplo de campo string para cada campo"
palavras =texto.split(" ")
contagem = {}

for palavras in contagem:
    if palavras in contagem:
        contagem[palavras] = +1
    else:
        contagem[palavras] = 1

print(contagem)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

numeros = [10, 20, 30, 40, 50]
minimo = min(numeros)
maximo = max(numeros)
normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

print(normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
dados_usuarios = [
    {"produto": "Maquina de Lavar", "codigo": "123"},
    {"produto": "Geladeira", "codigo": ""},
    {"produto": "Ferro de passar", "codigo": "258"}
]

verificacao = [dados for dados in dados_usuarios if dados["codigo"]]
print(verificacao)
### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.