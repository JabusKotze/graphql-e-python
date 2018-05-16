Lead CRUD
=========

Objetivo
--------

Esse é um primeiro exemplo de um projeto completo utilizando:

    * Python3.x (x>=6)
    * Pyramid
    * Graphql (graphene)


Setup
-----

Esses são os passos que você precisa executar para utilizar o projeto
    * Criar um virtualenv
        mkproject -p $(which python3)  # exemplo com virtualenvwrapper

    * Instalar o projeto e suas dependencias
        pip install -e ".[testing]"

    * Configurar o banco de dados
        initialize_lead_crud_db development.ini

    * [TODO] Executar os testes

    * Executar o projeto
        pserve development.ini


Com a aplicação em execução, você deve conseguir acessar o endpoint `http://0.0.0.0:6543/api/v1/graphql`. Nesse endpoint, você terá acesso ao `GraphiQL` - uma interface para executar queries, mutations  e etc.
