 P1 - API de Gestão de Tarefas

Este projeto é uma API desenvolvida com **Django** para o gerenciamento de tarefas, permitindo vincular usuários responsáveis a cada atividade.
Tecnologias Utilizadas
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [SQLite](https://www.sqlite.org/index.html) (Banco de dados local)

## 📋 Requisitos Implementados
1.  **App Usuarios**: Criação de um novo app para gestão de pessoas.
2.  **Model Usuario**: Campos para nome, e-mail único e status.
3.  **Relacionamento**: Chave estrangeira (ForeignKey) ligando Tarefas a Usuários.
4.  **Admin Customizado**: Registro de todos os modelos no painel administrativo do Django.
5.  **Endpoints**:
    * `GET /usuarios/`: Lista todos os usuários.
    * `GET /usuarios/<id>/`: Busca um usuário específico por ID.
    * `GET /api/`: Lista tarefas exibindo o nome do usuário responsável.
