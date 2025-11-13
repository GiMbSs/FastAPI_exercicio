# FastAPI TODO App

Uma aplicação de gerenciamento de tarefas (TODO) construída com FastAPI, MongoDB e Beanie ODM.

## Características

- ✅ Autenticação JWT
- ✅ Gerenciamento de usuários
- ✅ CRUD completo de tarefas
- ✅ Relacionamentos entre usuários e tarefas
- ✅ Validação de dados com Pydantic
- ✅ Documentação automática com Swagger
- ✅ Docker e Docker Compose

## Requisitos

- Python 3.13+
- Docker e Docker Compose (opcional)
- MongoDB

## Instalação Local

### 1. Clonar o repositório

```bash
git clone <seu-repositorio>
cd FastAPI_exercicio
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instalar dependências

```bash
cd app
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
MONGO_CONNECTION_STRING=mongodb://localhost:27017/todoapp
JWT_SECRET_KEY=sua-chave-secreta-aqui
JWT_REFRESH_SECRET_KEY=sua-chave-refresh-secreta-aqui
```

### 5. Iniciar a aplicação

```bash
uvicorn app:app --reload
```

A aplicação estará disponível em `http://localhost:8000`

## Instalação com Docker

### 1. Build e iniciar containers

```bash
docker-compose up -d --build
```

### 2. Acessar a aplicação

- API: `http://localhost:8000`
- Swagger: `http://localhost:8000/docs`
- MongoDB: `localhost:27017`

### 3. Parar containers

```bash
docker-compose down
```

## Estrutura do Projeto

```
FastAPI_exercicio/
├── app/
│   ├── api/
│   │   ├── auth/
│   │   │   └── jwt.py          # Autenticação JWT
│   │   ├── depedencies/
│   │   │   └── user_deps.py    # Dependências de usuário
│   │   ├── handles/
│   │   │   ├── task.py         # Endpoints de tarefas
│   │   │   └── user.py         # Endpoints de usuários
│   │   └── router.py           # Roteador principal
│   ├── core/
│   │   ├── config.py           # Configurações
│   │   └── security.py         # Funções de segurança
│   ├── models/
│   │   ├── task_model.py       # Modelo Task (Beanie)
│   │   └── user_model.py       # Modelo User (Beanie)
│   ├── schemas/
│   │   ├── auth_schema.py      # Schema de autenticação
│   │   ├── task_schema.py      # Schema de tarefas
│   │   └── user_schema.py      # Schema de usuários
│   ├── services/
│   │   ├── task_service.py     # Lógica de tarefas
│   │   └── user_service.py     # Lógica de usuários
│   └── app.py                  # Aplicação principal
├── requirements.txt            # Dependências Python
├── Dockerfile                  # Configuração Docker
├── docker-compose.yml          # Orquestração Docker
├── .gitignore                  # Git ignore
├── .dockerignore                # Docker ignore
└── README.md                   # Este arquivo
```

## Endpoints da API

### Autenticação

- `POST /api/v1/auth/login` - Login e obter tokens
- `POST /api/v1/auth/test-token` - Testar token JWT

### Usuários

- `POST /api/v1/user/add` - Criar novo usuário

### Tarefas

- `GET /api/v1/task/` - Listar todas as tarefas
- `GET /api/v1/task/{task_id}` - Obter detalhes de uma tarefa
- `POST /api/v1/task/create` - Criar nova tarefa
- `PUT /api/v1/task/{task_id}` - Atualizar tarefa
- `DELETE /api/v1/task/{task_id}` - Deletar tarefa

## Documentação Interativa

Acesse a documentação Swagger em:
```
http://localhost:8000/docs
```

## Fluxo de Uso

1. **Criar usuário**: `POST /api/v1/user/add`
   ```json
   {
     "email": "usuario@example.com",
     "username": "meu_usuario",
     "password": "senha123"
   }
   ```

2. **Login**: `POST /api/v1/auth/login`
   - Usar `application/x-www-form-urlencoded`
   - Campos: `username`, `password`, `grant_type=password`

3. **Criar tarefa**: `POST /api/v1/task/create` (com Bearer token)
   ```json
   {
     "title": "Minha tarefa",
     "description": "Descrição da tarefa",
     "status": false
   }
   ```

4. **Listar tarefas**: `GET /api/v1/task/` (com Bearer token)

5. **Atualizar tarefa**: `PUT /api/v1/task/{task_id}` (com Bearer token)
   ```json
   {
     "status": true
   }
   ```

6. **Deletar tarefa**: `DELETE /api/v1/task/{task_id}` (com Bearer token)

## Tecnologias Utilizadas

- **FastAPI**: Framework web moderno
- **Pydantic**: Validação de dados
- **MongoDB**: Banco de dados NoSQL
- **Beanie ODM**: Object Document Mapper para MongoDB
- **PyJWT**: Autenticação JWT
- **Passlib + Bcrypt**: Hash de senhas
- **Motor**: Driver assíncrono para MongoDB
- **Uvicorn**: Servidor ASGI

## Variáveis de Ambiente

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| `MONGO_CONNECTION_STRING` | String de conexão MongoDB | - |
| `JWT_SECRET_KEY` | Chave secreta JWT | - |
| `JWT_REFRESH_SECRET_KEY` | Chave refresh JWT | - |
| `ALGORITHM` | Algoritmo JWT | HS256 |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Expiração token (minutos) | 60 |
| `REFRESH_TOKENS_EXPIRE_MINUTES` | Expiração refresh (minutos) | 10080 |

## Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT.

## Contato

Para dúvidas ou sugestões, abra uma issue no repositório.

