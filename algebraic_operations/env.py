"""

This module defines a configuration class for handling environment variables and settings.
"""

import os


class Env:
    """
    Encapsulates various configuration parameters using environment variables.

    Attributes:
        - SECRET_KEY (str): Secret key for the application. Default is 'secret_key'.
        - DEBUG (bool): Debug mode flag, parsed from the 'DEBUG' environment variable.
            Default is True.
        - ALLOWED_HOSTS (list): List of allowed hosts for the application, parsed
            from the 'ALLOWED_HOSTS' environment variable. Default is ['localhost'].
        - DATABASE_URL (str): URL for the database connection, parsed from the
            'DATABASE_URL' environment variable. Default is an empty string.
        - DATABASE_NAME (str): Name of the database, parsed from the 'DATABASE_NAME'
            environment variable. Default is 'algebraic_db'.
        - ENVIRONMENT (str): Current environment mode, parsed from the 'ENVIRONMENT'
            environment variable. Default is 'development'.
    """
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key')
    DEBUG = bool(int(os.getenv('DEBUG', '1')))
    DATABASE_URL = os.getenv('DATABASE_URL', '')
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'algebraic_db')
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
