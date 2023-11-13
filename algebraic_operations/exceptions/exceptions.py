from rest_framework import status
from rest_framework.exceptions import APIException


class UnsupportedFunction(APIException):
    """
    An exception raised when an unsupported function is encountered.

    Attributes:
        status_code (int): The HTTP status code for the exception.
        default_detail (str): The default error message for this exception.
    """
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Unsupported function.'


class DivisionByZero(APIException):
    """
    An exception raised when a division by zero is attempted.

    Attributes:
        status_code (int): The HTTP status code for the exception.
        default_detail (str): The default error message for this exception.
    """
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Division by zero.'


class InvalidExpression(APIException):
    """
    An exception raised when an invalid expression is encountered.

    Attributes:
        status_code (int): The HTTP status code for the exception.
        default_detail (str): The default error message for this exception.
    """
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Invalid Expression.'


class PaginatorError(APIException):
    """
    An exception raised when there is an issue with pagination parameters.

    Attributes:
        status_code (int): The HTTP status code for the exception.
        default_detail (str): The default error message for this exception.
    """
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Both page_number and page_size should be provided or both should be null.'
