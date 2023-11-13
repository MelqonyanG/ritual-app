# Algebraic Expressions

Djnago application that allows users to efficiently evaluate algebraic expressions, using Django Framework, see the result of the evaluation and view a history of operations.

# Usage
## Endpoints

### /docs
Description: Access the Swagger documentation page for detailed API information and usage.

Method: GET

Open this endpoint in a web browser to interact with and understand the available endpoints and their functionalities.


### /history
Method: GET

Parameters: page_size and page_number (optional)

Description: Retrieve the history of operations with pagination support.

Request Example:

Get: /history?page_number=1&page_size=2

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

Description: Submit algebraic expressions for evaluation.


Request example:

POST: /evaluate

Body (json):
```
{
    "expression": "3 + abs(-5) * len('hello')"
}
```

Response:
```
{
    "result": 28
}
```


# Technologies Used
- Django Framework
- PostgreSQL


# Setup and Running
This application is Dockerized and uses Docker Compose for setup. To run the application:

- Make sure Docker and Docker Compose are installed.
- Clone the [repository](https://github.com/MelqonyanG/ritual-app.git).
- Navigate to the project directory.
- Run **docker-compose up** to start the application.

# Accessing Swagger Documentation
Once the application is running, access the Swagger documentation by navigating to http://your_server_address/docs in your web browser.

This documentation will provide detailed information on the available endpoints, their functionalities, request formats, and response structures.


# Testing
Run test inside the docker container by calling
```
python manage.py tests
```

