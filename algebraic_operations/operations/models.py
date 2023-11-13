from django.db import models

class Operation(models.Model):
    """
    Represents an operation in the system.

    Fields:
        expression (CharField): Represents the mathematical expression.
        result (FloatField): Represents the result of the expression.
        timestamp (DateTimeField): Represents the timestamp of the operation.
    """

    expression = models.CharField(max_length=255)
    result = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
