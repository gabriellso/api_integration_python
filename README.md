# 🚀 API Integration – Python + REST + PostgreSQL

Integração completa entre Python, API REST e banco de dados PostgreSQL (via Docker).  
O projeto consome dados externos, normaliza o JSON e persiste as informações no banco.

---

## 📌 Funcionalidades

- 🔗 Consumo de API REST (GET/POST)
- 🔐 Autenticação via Token
- 🧹 Tratamento e padronização de respostas JSON
- 🗄️ Armazenamento no PostgreSQL usando `psycopg2`
- 🧩 Estrutura profissional de módulos
- 🐳 Banco totalmente isolado via Docker

---

## ⚙️ Como Executar o Projeto

### **1. Instale as dependências**

```bash
pip install -r requirements.txt
```

### **2. Configure o arquivo .env**

Crie um arquivo .env com:
```bash
API_URL=https://jsonplaceholder.typicode.com/users
API_TOKEN=

DB_HOST=localhost
DB_PORT=5432
DB_NAME=api_integration
DB_USER=postgres
DB_PASSWORD=123456
```

⚠️ Observação: .env NÃO é commitado (está no .gitignore)

### **3. Suba o PostgreSQL com Docker**
```bash
docker run --name postgres_api \
  -e POSTGRES_PASSWORD=123456 \
  -e POSTGRES_DB=api_integration \
  -p 5432:5432 \
  -d postgres:16
```

### **4. Execute o projeto**
```bash
python main.py
```

### **🧪 Testar o Banco**

Acessar o banco dentro do container:
```bash
docker exec -it postgres_api psql -U postgres -d api_integration
```

Listar usuários:
```bash
SELECT * FROM users;
```
