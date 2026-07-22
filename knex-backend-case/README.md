# TechMart API

API REST desenvolvida como solução para o desafio técnico de Desenvolvedor Backend da KNEX Consultoria Jr.

## Tecnologias utilizadas

* Python 3.12+
* FastAPI
* SQLite
* JWT (PyJWT)
* Argon2 (hash de senhas)

## Decisões técnicas

### FastAPI

Escolhi o FastAPI por ser um framework moderno para desenvolvimento de APIs REST, oferecendo boa performance, documentação automática e uma estrutura simples para organizar o projeto, além de já ter experiência com um framework similar (Flask)

### SQLite

Foi utilizado SQLite por ser um banco de dados leve e suficiente para o escopo do desafio, não exigindo instalação de um servidor de banco de dados.

### Organização do projeto

O projeto foi separado em camadas para facilitar manutenção e evolução.

```
app/
├── database/
│
├── routes/
│
├── services/
│
├── security/
│
├── schemas/
│
└── main.py
│
└── exception.py
│
└── config.py
```

Cada camada possui uma responsabilidade específica:

* **routes**: define os endpoints da API.
* **services**: contém as regras de negócio.
* **database/repository**: realiza acesso ao banco de dados.
* **security**: autenticação, JWT e hash de senhas.
* **schemas**: modelos de entrada e saída da API.
* **exception**: lança as execeções http
* **config**: pega as variáveis de ambiente

---

# Como executar o projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git

cd SEU_REPOSITORIO
```

## 2. Criar ambiente virtual

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

## 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

## 4. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto.

Exemplo:

```env
SECRET_PEPPER=sua_chave_pepper

SECRET_KEY_JWT=sua_chave_jwt

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60
```

## 5. Executar a aplicação

```bash
uvicorn app.main:app --reload
```

A API ficará disponível em:

```
http://localhost:8000
```

---

# Documentação da API

Após iniciar o servidor, a documentação automática pode ser acessada em:

Swagger UI

```
http://localhost:8000/docs
```

ou

ReDoc

```
http://localhost:8000/redoc
```

---

# Como testar

A forma mais simples é utilizando o Swagger.

1. Crie um usuário.
2. Faça login.
3. Copie o token JWT retornado.
4. Clique em **Authorize**.
5. Informe:

```
Bearer SEU_TOKEN
```

6. Teste as rotas protegidas.

---

# Autor

Vilmar Filho
