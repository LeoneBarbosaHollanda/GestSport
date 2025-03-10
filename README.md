# 🚀 Como Rodar o Projeto

## 📌 Pré-requisitos
Antes de começar, certifique-se de ter os seguintes itens instalados na sua máquina:

- **Python 3.12+** (caso esteja usando FastAPI)  
- **PostgreSQL ** (dependendo do banco escolhido)  
- **virtualenv** (para gerenciar dependências)  

---

## 🛠 Passos para Rodar o Projeto

### 1️⃣ Clone o repositório:
```bash
git clone https://github.com/LeoneBarbosaHollanda/GestSport.git
cd GestSport
```

### 2️⃣ Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/Scripts/activate  
or
.\venv\Scripts\activate

```
### 3️⃣ Instale as dependências:
```bash
pip install -r requirements.txt 
```

### 4️⃣ Configure as variáveis de ambiente:
Crie um arquivo `.env` na raiz do projeto e defina as configurações do banco de dados para que ele e as tabelas sejam criadas automaticamente. Exemplo:
```
SECRET_KEY=sua_chave_secreta_super_segura
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
USER=seu_usuario
PASSWORD=sua_senha
DB_NAME=GSDB
```

### 6️⃣ Rode o servidor:
```bash
uvicorn app.main:app --reload
```
Agora a API estará disponível em `http://127.0.0.1:8000`. 🚀





