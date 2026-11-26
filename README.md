# MiniBlog - Projeto 2

Projeto desenvolvido para a disciplina de Programação Web Back-End, do curso de Sistemas de Informação da UTFPR.

O MiniBlog é uma aplicação web que permite consultar usuários, visualizar perfis e publicações, além de realizar autenticação de usuários.

## Tecnologias utilizadas

- Python
- Flask
- MySQL
- HTML
- CSS
- JavaScript

## Estrutura do projeto

```text
Projeto2_BackEnd/
├── app.py
├── config.py
├── database.py
├── controllers/
├── models/
├── routes/
├── templates/
└── static/
```

## Funcionalidades

- Busca de usuários por nome ou username.
- Consulta de perfil de usuário.
- Visualização das publicações de cada usuário.
- Login e logout.
- Controle de sessão.
- Proteção CSRF nas operações de autenticação.

## Como executar o projeto

1. Clone o repositório:

```bash
git clone https://github.com/claratarga/Projeto2_BackEnd.git
```

2. Entre na pasta:

```bash
cd Projeto2_BackEnd
```

3. Crie e ative o ambiente virtual:

```bash
python -m venv venv
```

No Windows:

```powershell
venv\Scripts\activate
```

4. Instale as dependências:

```bash
pip install Flask mysql-connector-python
```

5. Configure as variáveis de ambiente:

- `DB_HOST`: endereço do banco de dados.
- `DB_USER`: usuário do MySQL.
- `DB_PASSWORD`: senha do MySQL.
- `DB_NAME`: nome do banco de dados.
- `SECRET_KEY`: chave secreta da aplicação.

6. Execute a aplicação:

```bash
python app.py
```

A aplicação estará disponível em `http://127.0.0.1:5000`.

## Autoria

Projeto acadêmico desenvolvido em dupla para a disciplina de Programação Web Back-End.