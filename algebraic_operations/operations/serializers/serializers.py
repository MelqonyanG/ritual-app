from rest_framework import serializers
from algebraic_operations.operations.models import Operation
from algebraic_operations.exceptions import PaginatorError

class OperationSerializer(serializers.Serializer):
    expression = serializers.CharField()

class HistoryRequestSerializer(serializers.Serializer):
    page_number = serializers.IntegerField(allow_null=True, required=False)
    page_size = serializers.IntegerField(allow_null=True, required=False)

    def validate(self, data):
        page_number = data.get('page_number')
        page_size = data.get('page_size')

        if (page_number is None and page_size is not None) or (page_number is not None and page_size is None):
            raise PaginatorError
        
        return data

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'
