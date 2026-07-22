# TechMart API

API REST desenvolvida como solução para o desafio técnico de Desenvolvedor Backend da KNEX Consultoria Jr.

A aplicação consiste em uma API para gerenciamento de produtos e vendas de uma loja virtual, com autenticação de usuários e controle de estoque.

## Tecnologias utilizadas

* Python 3.12+
* FastAPI
* SQLite
* Docker
* JWT (PyJWT)
* Argon2 (hash de senhas)

---

# Decisões técnicas

## FastAPI

Escolhi o FastAPI por ser um framework moderno para desenvolvimento de APIs REST, oferecendo boa performance, documentação automática e uma estrutura simples para organização do projeto, além de já possuir experiência com um framework similar (Flask).

## SQLite

Foi utilizado SQLite por ser um banco de dados leve e suficiente para o escopo do desafio, não exigindo instalação de um servidor de banco de dados externo.

## Docker

Foi utilizado Docker para facilitar a execução da aplicação em diferentes ambientes, garantindo que as dependências necessárias estejam isoladas e padronizadas.

## Organização do projeto

O projeto foi separado em camadas para facilitar manutenção e evolução.

```
knex-backend-case/
│
├── database/
│
├── repository/
│
├── routes/
│
├── schemas/
│
├── security/
│
├── services/
│
├── config.py
├── exceptions.py
├── main.py
│
├── Dockerfile
├── requirements.txt
└── .env.example
```

Cada camada possui uma responsabilidade específica:

* **routes**: define os endpoints da API.
* **services**: contém as regras de negócio da aplicação.
* **repository**: realiza o acesso e manipulação dos dados.
* **database**: contém a configuração e conexão com o banco de dados.
* **security**: autenticação, JWT e hash de senhas.
* **schemas**: modelos de entrada e saída da API.
* **exceptions**: tratamento de exceções HTTP.
* **config**: gerenciamento das variáveis de ambiente.

---

# Como executar o projeto

## Opção 1: Executando com Docker

### Pré-requisitos

- Docker instalado.

### 1. Configurar variáveis de ambiente

Crie um arquivo `.env` baseado no arquivo `.env.example`.

Exemplo:

```env
SECRET_PEPPER=sua_chave_pepper

SECRET_KEY_JWT=sua_chave_jwt

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### 2. Criar a imagem Docker

Na raiz do projeto:

```bash
docker build -t techmart-api .
```

### 3. Executar o container

```bash
docker run --env-file .env -p 8000:8000 techmart-api
```

A API estará disponível em:

```
http://localhost:8000
```

---

## Opção 2: Executando localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git

cd knex-backend-case
```

### 2. Criar ambiente virtual

Windows:

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto baseado no `.env.example`.

### 5. Executar a aplicação

```bash
uvicorn main:app --reload
```

A API estará disponível em:

```
http://localhost:8000
```

---

# Documentação da API

A documentação automática do FastAPI está disponível em:

## Swagger UI

```
http://localhost:8000/docs
```

## ReDoc

```
http://localhost:8000/redoc
```

---

# Como testar

A forma mais simples de testar a API é utilizando o Swagger.

1. Crie um usuário.
2. Faça login.
3. Copie o token JWT retornado.
4. Clique em **Authorize**.
5. Informe:

```
Bearer SEU_TOKEN
```

6. Execute as rotas protegidas.

---

# Autor

Vilmar Filho