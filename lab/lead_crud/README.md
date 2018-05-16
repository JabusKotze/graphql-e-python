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


Com a aplicação em execução, você deve conseguir acessar o endpoint `http://0.0.0.0:6543/api/v1/graphql`.
Nesse endpoint, você terá acesso ao `GraphiQL` - uma interface para executar queries, mutations  e etc.


Exemplo de queries e mutations
------------------------------

* Recuperar `uuid`, `name` e `email`

    ```graphql
    {
        leads {
            uuid
            name
            email
        }
    }
    ```

* Criar um novo lead:

    ```graphql
        mutation {
            newLead(
                input:{
                    name: "Houston hero", cpf: "41083499890", product: "lead-app",
                    email: "foo@bar.bleh", employmentSalary:"5000", loanPrincipal: "500000", loanReason: "GimmeMoney",
                    loanInstalmentNumber: "12", clientMutationId: "foo"
                }
            ){
                lead {
                    uuid
                }
            }
        }
    ```

* Atualizar um lead:

    ```graphql
        mutation{
          updateLead(input: {uuid: "a1a6f201f0eb4bf5ba261557aef9db26", name:"Name without typo"}) {
            lead{
              name
            }
          }
        }
    ```

* Excluir um lead:

    ```graphql
        mutation{
          updateLead(input: {uuid: "a1a6f201f0eb4bf5ba261557aef9db26", name:"Name without typo"}) {
          }
        }
    ```
