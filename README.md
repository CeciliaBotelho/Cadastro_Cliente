# Client Register

"Client Register" é uma aplicação web desenvolvida utilizando o framework Django, projetada para facilitar o gerenciamento de clientes por parte de empresas ou profissionais autônomos. Esta plataforma intuitiva permite aos funcionarios realizar operações essenciais de cadastro de clientes, tais como adicionar, atualizar, visualizar e excluir informações de clientes de maneira eficiente. Além disso, "Client Register" incorpora técnicas de lógica fuzzy por meio da biblioteca `scikit-fuzzy`, permitindo uma tomada de decisão mais refinada e adaptativa em relação à classificação e ao tratamento dos dados dos clientes.

A lógica fuzzy é aplicada no projeto para lidar com categorizações e decisões que não são absolutas, simulando uma forma de raciocínio mais próxima da humana, o que é particularmente útil para definir personalizar serviços baseados em perfis de clientes complexos e variáveis.

## Começando

Estas instruções fornecerão uma cópia do projeto em execução na sua máquina local para fins de desenvolvimento e teste. Veja as notas sobre como implantar o projeto em um sistema ao vivo.

### Pré-requisitos

Antes de começar, certifique-se de ter o Python 3.8 ou superior instalado em sua máquina. Além disso, você precisará do Django 5.0.3 e da biblioteca `scikit-fuzzy` para executar este projeto.

### Instalando

Siga estes passos para obter um ambiente de desenvolvimento em execução:

1. Clone o repositório:

git clone https://seu-repositorio-aqui

csharp
Copy code

2. Instale as dependências do projeto utilizando o pip:

pip install -r requirements.txt


3. Realize as migrações necessárias para configurar seu banco de dados:

python manage.py migrate


4. Inicie o servidor de desenvolvimento:

python manage.py runserver

Agora, você deve ser capaz de acessar a aplicação através do endereço `http://127.0.0.1:8000/` no seu navegador.

## Rodando os Testes

Testes são uma parte crucial do desenvolvimento de software, garantindo que sua aplicação continue funcionando corretamente após mudanças e novas funcionalidades. No Django, você pode rodar os testes para seu projeto utilizando o seguinte comando:

python manage.py tests

Este comando irá procurar por arquivos de teste em seu projeto, executá-los e fornecer um relatório sobre os testes que passaram e os que falharam.

## Construído Com

- [Django](https://www.djangoproject.com/) - O framework web usado
- [NetworkX](https://networkx.org/) - Usado para criar e manipular estruturas de dados complexas
- [scikit-fuzzy](https://scikit-fuzzy.github.io/scikit-fuzzy/) - Usado para implementar lógica fuzzy no gerenciamento de clientes


## Autor

- **Cecilia Botelho** - *Teste* - [CeciliaBotelho]([https://github.com/SeuPerfil](https://github.com/CeciliaBotelho))

