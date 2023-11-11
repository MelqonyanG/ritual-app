from rest_framework import status
from rest_framework.exceptions import APIException


class UnsupportedFunction(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Unsupported function.'


class DivisionByZero(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Division by zero.'


class PaginatorError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Both page_number and page_size should be provided or both should be null.'