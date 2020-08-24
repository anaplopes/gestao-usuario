# Api Gestão Usuários

![](arquitetura_simplificada.png)

Steps to run this project:

1. You should run the containers and build the images
```shell
    docker-compose up --build
```

2. Then create db connection
- DRIVER: PostgreSQL
- HOST: db
- PORT: 5432
- DATABASE: usuarios
- USERNAME: postgres
- PASSWORD: secretpassword

3. To run project you must access
http://127.0.0.1:80/


## Endpoint:

### Status da API
| Methods  | Actions                   | Url                                         |
|:--------:|:--------------------------|:--------------------------------------------|
| GET      | status da api             | {{url}/                                     |

### Usuários
| Methods  | Actions                                    | Url                            |
|:--------:|:-------------------------------------------|:-------------------------------|
| GET      | retorna todos os usuários cadastrados      | {{url}}/user                   |
| POST     | permite criar um novo usuário              | {{url}}/user/create            |
| GET      | retorna um usuário específico              | {{url}}/user/{{id:uuid}}       |
| PUT      | permite editar um usuário específico       | {{url}}/user/{{id:uuid}}       |
| DELETE   | permite remover um usuário específico      | {{url}}/user/{{id:uuid}}       |
