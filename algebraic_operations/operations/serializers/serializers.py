from rest_framework import serializers
from algebraic_operations.operations.models import Operation
from algebraic_operations.exceptions import PaginatorError

class OperationSerializer(serializers.Serializer):
    """
    Serializer for handling algebraic operation expressions.

    Attributes:
        expression (CharField): A character field to represent the algebraic expression.
    """

    expression = serializers.CharField()


class HistoryRequestSerializer(serializers.Serializer):
    """
    Serializer for validating history request parameters.

    Attributes:
        page_number (IntegerField): Represents the page number for history.
        page_size (IntegerField): Represents the size of the page for history.

    Methods:
        validate(self, data): Custom validation method to check page number and page size.
    """

    page_number = serializers.IntegerField(allow_null=True, required=False)
    page_size = serializers.IntegerField(allow_null=True, required=False)

    def validate(self, data):
        """
        Validate the provided page_number and page_size.

        Args:
            data (dict): Input data containing page_number and page_size.

        Raises:
            PaginatorError: If page_number and page_size are inconsistent.

        Returns:
            dict: The validated data.
        """

        page_number = data.get('page_number')
        page_size = data.get('page_size')

        if any([
            page_number is None and page_size is not None,
            page_number is not None and page_size is None
        ]):
            raise PaginatorError

        return data


class HistorySerializer(serializers.ModelSerializer):
    """
    Serializer for handling history of algebraic operations.

    Attributes:
        Meta (class): Defines the metadata for the serializer.

    Meta:
        model (Operation): The model this serializer is based on.
        fields (str): Indicates all fields should be included.
    """

    class Meta:
        model = Operation
        fields = '__all__'
