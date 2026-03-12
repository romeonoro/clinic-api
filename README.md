# 🏥 Clinic API

API REST para gerenciamento de uma clínica médica desenvolvida com **Python, Django e Django REST Framework**.

Este projeto demonstra a construção de um *backend* moderno com:

* API REST
* Autenticação JWT
* Documentação automática da API
* Organização em camadas
* Boas práticas de desenvolvimento backend

O sistema permite o gerenciamento de **pacientes, médicos e consultas**, simulando um ambiente real de clínica médica.

---

# 🚀 Tecnologias Utilizadas

* Python
* Django
* Django REST Framework
* JWT Authentication
* Swagger / OpenAPI
* SQLite
* Git

---

# 📦 Funcionalidades

## 👨‍⚕️ Médicos

* Cadastro de médicos
* Listagem de médicos
* Atualização de informações
* Remoção de médicos

## 🧑‍💼 Pacientes

* Cadastro de pacientes
* Listagem de pacientes
* Atualização de dados
* Remoção de pacientes

## 📅 Consultas

* Agendamento de consultas
* Associação entre paciente e médico
* Controle de disponibilidade de horário

## 🔐 Autenticação

A API utiliza autenticação baseada em **JWT (JSON Web Token)** para proteger endpoints.

Isso garante que apenas usuários autenticados possam acessar determinadas rotas da API.

---

# 📚 Documentação da API

A API possui documentação interativa gerada automaticamente.

Após rodar o projeto, você poderá acessar:

### Swagger UI

```
http://127.0.0.1:8000/swagger/
```

### ReDoc

```
http://127.0.0.1:8000/redoc/
```

Essas interfaces permitem:

* visualizar todos os endpoints
* testar requisições diretamente no navegador
* ver parâmetros de entrada
* analisar respostas da API

---

# 🔐 Autenticação JWT

Para acessar endpoints protegidos, é necessário gerar um token de autenticação.

## Gerar token

Endpoint:

```
POST /api/token/
```

Exemplo de requisição:

```json
{
  "username": "admin",
  "password": "123456"
}
```

Resposta:

```json
{
  "refresh": "TOKEN",
  "access": "TOKEN"
}
```

---

## Utilizar token

Nas requisições autenticadas, inclua o header:

```
Authorization: Bearer SEU_TOKEN
```

Exemplo:

```
GET /api/patients
```

Header:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

# 🏗 Estrutura do Projeto

```
clinic-api
│
├── appointments
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── services.py
│
├── doctors
│   ├── models.py
│   ├── serializers.py
│   └── views.py
│
├── patients
│   ├── models.py
│   ├── serializers.py
│   └── views.py
│
├── config
│   ├── settings.py
│   └── urls.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🧠 Arquitetura

O projeto segue uma separação clara de responsabilidades:

### Models

Responsáveis pela estrutura do banco de dados.

### Serializers

Transformam objetos Python em JSON e vice-versa.

### Views

Responsáveis pelos endpoints da API.

### Services

Camada responsável pelas regras de negócio, mantendo as views mais organizadas.

Exemplo de regra implementada:

* Verificar se um médico já possui consulta agendada no mesmo horário antes de permitir novo agendamento.

---

# ⚙️ Como Rodar o Projeto

## 1️⃣ Clonar o repositório

```
git clone https://github.com/SEU_USUARIO/clinic-api.git
```

Entrar na pasta:

```
cd clinic-api
```

---

## 2️⃣ Criar ambiente virtual

```
python -m venv venv
```

---

## 3️⃣ Ativar ambiente virtual

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

## 4️⃣ Instalar dependências

```
pip install -r requirements.txt
```

---

## 5️⃣ Rodar migrações

```
python manage.py migrate
```

---

## 6️⃣ Criar usuário administrador

```
python manage.py createsuperuser
```

---

## 7️⃣ Iniciar servidor

```
python manage.py runserver
```

---

# 🌐 Acessar Aplicação

Após rodar o servidor:

Painel administrativo:

```
http://127.0.0.1:8000/admin
```

Documentação da API:

```
http://127.0.0.1:8000/swagger/
```

---

