
<a href="https://www.fiap.com.br/">
<img src="img/fiap.png" width="140" height="50">
</a> <br>

<a href="https://www.instagram.com/fiapoficial/">
<img src="img/ig.png">
</a>
<a href="https://www.youtube.com/@FiapBrasil">
<img src="img/yt.png">
</a>

 <br>


# Python App Monitor & Manager para Docker

Este software é uma ferramenta de linha de comando desenvolvida em Python, projetada para interagir com o Docker. Ele utiliza a API do Docker para executar várias operações, permitindo ao usuário uma interface amigável e intuitiva para gerenciar seus containers e imagens Docker.

- Editor Utilizado: <a href="https://code.visualstudio.com/"> Visual Studio Code</a>.

- [Video Explicativo](colocaolinkaq)

- <a href="https://www.canva.com/design/DAFf6JnZJlo/4dJEE_-mZoVnFcOLFnx_eA/view?utm_content=DAFf6JnZJlo&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink"> Slides
  </a><br>

## Características

- **Visualização de Containers**: Uma visão rápida de todos os containers Docker em execução ou parados.
- **Gestão de Containers**: Fornece funcionalidades para criar, iniciar, parar, reiniciar, matar e remover containers.
- **Logs e Processos**: Permite ao usuário visualizar logs de containers e processos em execução dentro de um container.
- **Gestão de Imagens**: Lista todas as imagens disponíveis e fornece uma opção para remover imagens.
- **Informações do Sistema**: Exibe informações sobre o sistema Docker e sua versão.
- **Monitoramento**: Oferece uma visão sobre o uso de dados e ping para verificar a acessibilidade do servidor Docker.
- **Interface Amigável**: A interface de linha de comando é colorida e claramente categorizada, tornando a navegação e a execução de tarefas uma brisa.

## Configuração

O endereço da API é definido através da biblioteca `decouple`, permitindo ao usuário uma fácil configuração através de variáveis de ambiente.


## Objetivo

Desenvolver um software em Python capaz de:

- Realizar operações básicas com containers e imagens.
- Visualizar estatísticas de uso dos containers gerenciados pelo Docker Engine.

A manipulação e obtenção de dados dos containers devem ser realizadas através da **API do Docker**, com mensagens HTTP formatadas em JSON.

## Contextualização

Neste trabalho, o foco é no uso intensivo do Docker, onde uma aplicação é isolada em containers. Como exemplo, um sistema comercial com um banco de dados e três módulos rodaria em quatro containers distintos.

O Docker, originalmente baseado no LXC, evoluiu para ser uma solução multiplataforma, suportando tanto aplicações Windows quanto Linux


# **Resumo do Código**

### Importação de Bibliotecas e Configuração de Cores

```python
from decouple import config
import requests

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
```

**Explicação:** Inicialmente, as bibliotecas `decouple` e `requests` são importadas. A biblioteca `decouple` é usada para obter variáveis de ambiente ou valores de configuração, enquanto `requests` é uma biblioteca HTTP popular em Python. A classe `Colors` define sequências de escape ANSI para colorir o texto no terminal.

---

### Funções Auxiliares

```python
def line():
    print(f"=======================================================")

def enter_for_continue():
    line()
    input("Press" + Colors.BOLD + " ENTER " + Colors.ENDC + "for continue...")
```

**Explicação:** Há duas funções auxiliares definidas:

1. `line()`: Essa função simplesmente imprime uma linha de "=". 
2. `enter_for_continue()`: Imprime uma linha e depois pede ao usuário para pressionar ENTER, proporcionando uma pausa na execução.

---

### Interação com Docker via API

1. **Listando Containers**

    ```python
    def list_containers():
        print("Listing containers:")
        line()
        response = requests.get(f"{API_ADDRESS}/v1.43/containers/json?all=true").json()
        for container in response:
            print(Colors.GREEN + "Container:" + Colors.ENDC, container)
        enter_for_continue()
    ```

    **Explicação:** Esta função é responsável por listar todos os containers gerenciados pelo Docker Engine. Através de uma requisição GET à API do Docker, ela obtém informações sobre cada container e as imprime no console.

<br>

2. **Criando um Container**

    ```python
    def create_a_container():
        print("Creating a container:")
        line()
        response = requests.post(f"{API_ADDRESS}/v1.43/containers/create&Hostname=Renan&Image=httpd")
        print(Colors.GREEN + "Container created:" + Colors.ENDC, response.json(), response.status_code)
        enter_for_continue()
    ```

    **Explicação:** Esta função cria um novo container usando a imagem "httpd". Ela realiza uma requisição POST para a API do Docker, especificando os detalhes do novo container. A resposta da API, incluindo o código de status, é então impressa.

<br>

3. **Listando Processos em Execução Dentro de um Container**

    ```python
    def list_processes_running_inside_a_container():
        print("Listing all processes running inside a container:")
        line()
        all_containers = requests.get(f"{API_ADDRESS}/v1.43/containers/json?all=true").json()
        for container in all_containers:
            container_id = container["Id"]
            response = requests.get(f"{API_ADDRESS}/v1.43/containers/{container_id}/top").json()
            print(Colors.GREEN + "Processes:" + Colors.ENDC, response)
        enter_for_continue()
    ```

    **Explicação:** Esta função recupera e lista os processos em execução dentro de todos os containers. Primeiro, ela obtém a lista de todos os containers. Em seguida, para cada container, ela faz uma requisição à API do Docker para recuperar os processos em execução e os imprime no console.

<br>

4. **Obtendo Logs de um Container**

    ```python
    def get_container_log():
        print("Getting containers log:")
        line()
        all_containers = requests.get(f"{API_ADDRESS}/v1.43/containers/json?all=true").json()
        for container in all_containers:
            container_id = container["Id"]
            response = requests.get(f"{API_ADDRESS}/v1.43/containers/{container_id}/logs?follow=true&stdout=true").json()
            print(Colors.GREEN + "Logs:" + Colors.ENDC, response)
        enter_for_continue()
    ```

    **Explicação:** A função recupera e exibe os logs de todos os containers. Assim como na função anterior, ela começa obtendo uma lista de todos os containers. Para cada container, uma requisição é feita para recuperar seus logs, que são então impressos.

<br>

5. **Iniciando um Container**

    ```python
    def start_a_container():
        print("Starting a container:")
        line()
        container_id = input("ID or name of the container: ")
        response = requests.post(f"{API_ADDRESS}/v1.43/containers/{container_id}/start")
        print(Colors.GREEN + "Response:" + Colors.ENDC, response.status_code)
        enter_for_continue()
    ```

    **Explicação:** Esta função permite que o usuário inicie um container específico. O ID ou nome do container é solicitado ao usuário. Uma vez fornecido, uma requisição POST é feita para iniciar o container. A resposta (código de status) da API é impressa.

<br>

6. **Parando um Container**

    ```python
    def stop_a_container():
        print("Stopping a container:")
        line()
        container_id = input("ID or name of the container: ")
        response = requests.post(f"{API_ADDRESS}/v1.43/containers/{container_id}/stop")
        print(Colors.GREEN + "Response:" + Colors.ENDC, response.status_code)
        enter_for_continue()
    ```

    **Explicação:** Esta função permite que o usuário pare um container específico. Assim como na função anterior, o ID ou nome do container é solicitado ao usuário. Uma vez fornecido, uma requisição POST é feita para parar o container, e o código de status é impresso.

<br>

7. **Reiniciando um Container**

    ```python
    def restart_a_container():
        print("Restarting a container:")
        line()
        container_id = input("ID or name of the container: ")
        response = requests.post(f"{API_ADDRESS}/v1.43/containers/{container_id}/restart")
        print(Colors.GREEN + "Response:" + Colors.ENDC, response.status_code)
        enter_for_continue()
    ```

    **Explicação:** Esta função reinicia um container específico. O usuário deve fornecer o ID ou nome do container. A API Docker é então chamada para reiniciar esse container, e o código de status da operação é impresso.

<br>

8. **Matando um Container**

    ```python
    def kill_a_container():
        print("Killing a container:")
        line()
        container_id = input("ID or name of the container: ")
        response = requests.post(f"{API_ADDRESS}/v1.43/containers/{container_id}/kill")
        print(Colors.GREEN + "Response:" + Colors.ENDC, response.status_code)
        enter_for_continue()
    ```

    **Explicação:** Esta função mata um container. Ela é semelhante às funções anteriores de iniciar e parar, mas neste caso, força a terminação do container. Após obter o ID ou nome do container do usuário, a API Docker é chamada para matar o container, e o código de status é impresso.

<br>

9. **Removendo um Container**

    ```python
    def remove_a_container():
        print("Removing a container:")
        line()
        container_id = input("ID or name of the container: ")
        response = requests.delete(f"{API_ADDRESS}/v1.43/containers/{container_id}")
        print(Colors.GREEN + "Response:" + Colors.ENDC, response.status_code)
        enter_for_continue()
    ```

    **Explicação:** A função permite ao usuário remover um container. Depois de obter o ID ou nome do container do usuário, uma requisição DELETE é feita para a API Docker, e o código de status da operação é mostrado.

<br>

10. **Obtendo Informações do Sistema**

    ```python
    def get_system_information():
        print("Getting system information:")
        line()
        response = requests.get(f"{API_ADDRESS}/v1.43/info").json()
        print(Colors.GREEN + "System Information:" + Colors.ENDC, response)
        enter_for_continue()
    ```

    **Explicação:** Esta função recupera informações sobre o sistema Docker em execução. Uma requisição GET é feita para a API Docker, e as informações do sistema são impressas.

<br>

11. **Ping**

    ```python
    def ping():
        print("Ping:")
        line()
        response = requests.get(f"{API_ADDRESS}/v1.43/_ping").text
        print(Colors.GREEN + "Response:" + Colors.ENDC, response)
        enter_for_continue()
    ```

    **Explicação:** Esta função simplesmente faz um "ping" na API Docker para verificar sua acessibilidade. A resposta da API é impressa.

<br>

12. **Obtendo Informações de Uso de Dados**

    ```python
    def get_data_usage_information():
        print("Getting data usage information:")
        line()
        response = requests.get(f"{API_ADDRESS}/v1.43/system/df").json()
        print(Colors.GREEN + "Data Usage Information:" + Colors.ENDC, response)
        enter_for_continue()
    ```

    **Explicação:** Esta função recupera informações sobre o uso de dados do sistema Docker, incluindo informações sobre volumes, containers, etc. A resposta da API é impressa.

<br>

13. **Obtendo a Versão**

    ```python
    def get_version():
        print("Getting Docker version:")
        line()
        response = requests.get(f"{API_ADDRESS}/v1.43/version").json()
        print(Colors.GREEN + "Docker Version:" + Colors.ENDC, response)
        enter_for_continue()
    ```

    **Explicação:** Por último, esta função simplesmente recupera e exibe a versão do Docker em execução, utilizando uma chamada à API.

---

### **Configuração da API e Mensagem de Boas-Vindas**

```python
API_ADDRESS = config('API_ADDRESS')

line()
print(Colors.HEADER + "Welcome to Python App Monitor & Manager from Docker" + Colors.ENDC)
```

**Explicação:**  
O endereço da API é obtido da configuração e armazenado em `API_ADDRESS`. Uma linha é desenhada e uma mensagem de boas-vindas é exibida.

### **Menu Principal**

```python
while True:
    try:
        line()
        print("Select a option from interact with the Docker: ")
        print(Colors.BLUE + "[1] " + Colors.ENDC + "List containers")
        print(Colors.BLUE + "[2] " + Colors.ENDC + "Create a containers")
        print(Colors.BLUE + "[3] " + Colors.ENDC + "List processes running inside a container")
        print(Colors.BLUE + "[4] " + Colors.ENDC + "Get containers log")
        print(Colors.BLUE + "[5] " + Colors.ENDC + "Start a container")
        print(Colors.BLUE + "[6] " + Colors.ENDC + "Stop a container")
        print(Colors.BLUE + "[7] " + Colors.ENDC + "Restart a container")
        print(Colors.BLUE + "[8] " + Colors.ENDC + "Kill a container")
        print(Colors.BLUE + "[9] " + Colors.ENDC + "Remove a container")
        print(Colors.BLUE + "[10] " + Colors.ENDC + "List Images")
        print(Colors.BLUE + "[11] " + Colors.ENDC + "Remove an image")
        print(Colors.BLUE + "[12] " + Colors.ENDC + "Get system information")
        print(Colors.BLUE + "[13] " + Colors.ENDC + "Ping")
        print(Colors.BLUE + "[14] " + Colors.ENDC + "Get data usage information")
        print(Colors.BLUE + "[15] " + Colors.ENDC + "Get version")
        print(Colors.FAIL + "[99] " + Colors.ENDC + "Exit")
```

**Explicação:**  
Dentro de um loop infinito, é apresentado um menu ao usuário com várias opções relacionadas ao Docker. Cada opção é colorida para melhor destaque.

---

### **Captura e Processamento da Escolha do Usuário**

```python
user_response = int(input(": "))
line()

if user_response == 1:
    list_containers()
elif user_response == 2:
    create_a_container()
elif user_response == 3:
    list_processes_running_inside_a_container()
elif user_response == 4:
    get_container_log()
elif user_response == 5:
    start_a_container()
elif user_response == 6:
    stop_a_container()
elif user_response == 7:
    restart_a_container()
elif user_response == 8:
    kill_a_container()
elif user_response == 9:
    remove_a_container()
elif user_response == 10:
    list_images()
elif user_response == 11:
    remove_a_image()
elif user_response == 12:
    get_system_information()
elif user_response == 13:
    ping()
elif user_response == 14:
    get_data_usage_information()
elif user_response == 15:
    get_version()
elif user_response == 99:
    break
else:
    print(Colors.FAIL + "Invalid option" + Colors.ENDC)
```

**Explicação:**  
O programa aguarda uma resposta do usuário e tenta convertê-la em um número inteiro. Com base nessa entrada, o programa chama uma função específica relacionada à opção escolhida. Se o usuário inserir `99`, o loop é encerrado. Qualquer outra entrada fora das opções listadas resultará na mensagem "Invalid option".

---

**Tratamento de Exceções**

```python
except ValueError:
    line()
    print(Colors.FAIL + "Invalid option" + Colors.ENDC)
except:
    line()
    print(Colors.FAIL + "Unexpected error" + Colors.ENDC)
```

**Explicação:**  
Existem tratamentos de exceções para capturar erros específicos. Se o usuário inserir uma entrada que não possa ser convertida para um número inteiro, o programa exibirá a mensagem "Invalid option". Qualquer outra exceção desconhecida resultará na mensagem "Unexpected error".



# **Conclusão**

O script apresentado é uma interface de linha de comando para gerenciar operações do Docker. Ele oferece ao usuário uma variedade de opções, desde listar contêineres, criar contêineres, até obter logs e informações do sistema. Toda a lógica de execução é estruturada em um loop contínuo, permitindo ao usuário realizar várias operações sem ter que reiniciar o script.

O design do código é intuitivo e modular, com cada funcionalidade encapsulada em sua própria função. Isso não só torna o código mais organizado, mas também facilita a manutenção e possíveis expansões futuras.

O tratamento de exceções garante que a aplicação lidará com entradas inesperadas e erros sem falhas catastróficas, melhorando a experiência do usuário e a robustez da aplicação.

Em resumo, o programa é uma ferramenta valiosa para qualquer pessoa ou equipe que trabalhe com Docker regularmente, simplificando e acelerando tarefas rotineiras.



# Contribuidores

<a href="https://github.com/Jogaridu"> Jorge Gabriel Ricci Dutra</a>,<a href="https://github.com/Aykie"> Júlia Barboza Brunelli</a>, <a href="https://github.com/NCalegariS"> Nicholas Calegari</a> e <a href="https://github.com/WHrez1ns"> Renan Dias</a>
<br>
**RM: 551457,98558, 93912 e 99258.**
