MiniBlog - Projeto 2

Projeto desenvolvido para a disciplina de Programação Web Back-End, do curso de Sistemas de Informação da UTFPR.

O MiniBlog é uma aplicação web que permite consultar usuários, visualizar perfis e publicações, além de realizar autenticação de usuários.

Tecnologias utilizadas

Python

Flask

MySQL

HTML

CSS

JavaScript

Estrutura do projeto

Projeto2_BackEnd/
├── app.py
├── config.py
├── database.py
├── controllers/
├── models/
├── routes/
├── templates/
└── static/

Funcionalidades

Busca de usuários por nome ou username.

Consulta de perfil de usuário.

Visualização das publicações de cada usuário.

Login e logout.

Controle de sessão.

Proteção CSRF nas operações de autenticação.

Como executar o projeto

Clone o repositório:

git clone https://github.com/claratarga/Projeto2_BackEnd.git

Entre na pasta:

cd Projeto2_BackEnd

Crie e ative o ambiente virtual:

python -m venv venv

No Windows:

venv\Scripts\activate

Instale as dependências:

pip install Flask mysql-connector-python

Configure as variáveis de ambiente:

DB_HOST: endereço do banco de dados.

DB_USER: usuário do MySQL.

DB_PASSWORD: senha do MySQL.

DB_NAME: nome do banco de dados.

SECRET_KEY: chave secreta da aplicação.

Execute a aplicação:

python app.py

A aplicação estará disponível em http://127.0.0.1:5000.

Autoria

Projeto acadêmico desenvolvido em dupla para a disciplina de Programação Web Back-End.