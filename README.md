# API Integration with Python + REST + PostgreSQL

Projeto de integração com API REST usando Python, com:

- Requests GET/POST
- Autenticação via Token
- Tratamento e normalização de JSON
- Armazenamento em banco PostgreSQL (Docker)
- Estrutura profissional de módulos

## Executando o projeto

### 1. Instale dependências
pip install -r requirements.txt

### 2. Configure o arquivo `.env`
API_URL=https://jsonplaceholder.typicode.com/users

API_TOKEN=

DB_HOST=localhost
DB_PORT=5432
DB_NAME=api_integration
DB_USER=postgres
DB_PASSWORD=123456

### 3. Suba o Postgres com Docker
docker run --name postgres_api ^
-e POSTGRES_PASSWORD=123456 ^
-e POSTGRES_DB=api_integration ^
-p 5432:5432 ^
-d postgres:16

### 4. Rodar o projeto
python main.py