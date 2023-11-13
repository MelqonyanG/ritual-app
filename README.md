# Algebraic Expressions

Djnago application that allows users to efficiently evaluate algebraic expressions, using Django Framework, see the result of the evaluation and view a history of operations.

# Usage
## Endpoints

### /history
Method: GET
Parameters: page_size and page_number (optional)
Description: Retrieve the history of operations with pagination support.
Response:
```
{
    "history": [
        {
            "id": 1,
            "expression": "3 + abs(-5) * len('hello')",
            "result": 28.0,
            "timestamp": "2023-11-13T07:59:33.052086Z"
        },
        {
            "id": 2,
            "expression": "3 + abs(-5) * len('hello')",
            "result": 28.0,
            "timestamp": "2023-11-13T07:59:38.572874Z"
        }
    ]
}
```


### /evaluate
Method: POST
Body: 
```
{
    "expression": "3 + abs(-5) * len('hello')"
}
```
Description: Submit algebraic expressions for evaluation.
Response:
```
{
    "result": 28
}
```


# Technologies Used
Django Framework
PostgreSQL


# Setup and Running
This application is Dockerized and uses Docker Compose for setup. To run the application:

- Make sure Docker and Docker Compose are installed.
- Clone the [repository](https://github.com/MelqonyanG/ritual-app.git).
- Navigate to the project directory.
- Run **docker-compose up** to start the application.

